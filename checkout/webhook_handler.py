from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import logging

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time
from decimal import Decimal

logger = logging.getLogger(__name__)

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email after successful order."""
        cust_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order},
        )
        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event from Stripe."""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook.

        Verifies if order exists by stripe_pid; creates one if not.
        Sends confirmation email after success.
        """
        intent = event.data.object
        pid = intent.id

        bag = getattr(intent.metadata, "bag", "{}")
        save_info = getattr(intent.metadata, "save_info", "false")
        username = getattr(intent.metadata, "username", "AnonymousUser")

        logger.info(f">>> Metadata received in webhook: {intent.metadata}")

        charges = getattr(intent, "charges", None)
        if charges and charges.data and len(charges.data) > 0:
            billing_details = charges.data[0].billing_details
        else:
            billing_details = getattr(intent, "billing_details", None)

        shipping_details = intent.shipping
        if not shipping_details or not shipping_details.address:
            return HttpResponse(
                content="Webhook received but shipping details missing.", status=400
            )

        # Clean empty shipping address fields
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        phone_number = shipping_details.phone or ""
        email = billing_details.email if billing_details and billing_details.email else ""

        profile = None
        if username != "AnonymousUser":
            try:
                profile = UserProfile.objects.get(user__username=username)
                if save_info == "true":
                    profile.default_phone_number = phone_number
                    profile.default_country = shipping_details.address.country
                    profile.default_postcode = shipping_details.address.postal_code
                    profile.default_town_or_city = shipping_details.address.city
                    profile.default_street_address1 = shipping_details.address.line1
                    profile.default_street_address2 = shipping_details.address.line2
                    profile.default_county = shipping_details.address.state
                    profile.save()
            except UserProfile.DoesNotExist:
                profile = None

        # Check if order exists by stripe_pid only
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(stripe_pid=pid)
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200,
            )
        else:
            order = None
            try:
                bag_dict = json.loads(bag)
                order_total = Decimal("0.00")

                for item_id, item_data in bag_dict.items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_total += product.price * item_data
                    else:
                        for size, quantity in item_data.get("items_by_size", {}).items():
                            order_total += product.price * quantity

                if order_total < Decimal(settings.FREE_DELIVERY_THRESHOLD):
                    delivery_cost = order_total * (
                        Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / Decimal("100")
                    )
                else:
                    delivery_cost = Decimal("0.00")

                grand_total = order_total + delivery_cost

                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=email,
                    phone_number=phone_number,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    delivery_cost=delivery_cost,
                    order_total=order_total,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )

                for item_id, item_data in bag_dict.items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                    else:
                        for size, quantity in item_data.get("items_by_size", {}).items():
                            OrderLineItem.objects.create(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
            except Exception as e:
                if order:
                    order.delete()
                logger.error(f"Error creating order from webhook: {e}")
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {str(e)}',
                    status=500,
                )

        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook.

        Logs the failure, does not create an order.
        """
        intent = event.data.object
        pid = intent.id
        error_message = intent.last_payment_error.message if intent.last_payment_error else "Unknown error"

        logger.warning(f"Payment failed for PaymentIntent {pid}. Reason: {error_message}")
        # You could add additional notifications here if desired

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | Payment failed handled', status=200
        )
