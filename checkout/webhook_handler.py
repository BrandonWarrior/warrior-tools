import json
import time
from decimal import Decimal
import logging
import traceback

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

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
        ).strip()  # Strip whitespace and newlines here to avoid BadHeaderError
        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )
        try:
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])
            logger.info(f"Confirmation email sent to {cust_email}")
        except Exception as e:
            logger.error(f"Failed to send confirmation email to {cust_email}: {e}")

    def handle_event(self, event):
        try:
            return HttpResponse(
                content=f'Unhandled webhook received: {event["type"]}', status=200
            )
        except Exception as e:
            logger.error(f"Exception in handle_event:\n{traceback.format_exc()}")
            return HttpResponse(content=f'Webhook handler error: {e}', status=500)

    def handle_payment_intent_succeeded(self, event):
        try:
            intent = event.data.object
            pid = intent.id

            bag = intent.metadata.get("bag", "{}")
            save_info = intent.metadata.get("save_info", "false")
            username = intent.metadata.get("username", "AnonymousUser")

            logger.info(f"Webhook received for PaymentIntent {pid} with metadata: {intent.metadata}")

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

            # Check if order exists by stripe_pid with retries
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
                        try:
                            product_id = int(item_id)
                            product = Product.objects.get(id=product_id)
                        except Product.DoesNotExist:
                            logger.error(f"Product with id {item_id} does not exist.")
                            raise
                        except Exception as e:
                            logger.error(f"Error retrieving product with id {item_id}: {e}")
                            raise

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
                        try:
                            product_id = int(item_id)
                            product = Product.objects.get(id=product_id)
                        except Product.DoesNotExist:
                            logger.error(f"Product with id {item_id} does not exist.")
                            raise
                        except Exception as e:
                            logger.error(f"Error retrieving product with id {item_id}: {e}")
                            raise

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
                    logger.error(f"Error creating order from webhook: {traceback.format_exc()}")
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500,
                    )

            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
                status=200,
            )

        except Exception as e:
            logger.error(f"Exception in handle_payment_intent_succeeded:\n{traceback.format_exc()}")
            return HttpResponse(content=f'Webhook handler error: {e}', status=500)

    def handle_payment_intent_payment_failed(self, event):
        try:
            intent = event.data.object
            pid = intent.id
            error_message = intent.last_payment_error.message if intent.last_payment_error else "Unknown error"

            logger.warning(f"Payment failed for PaymentIntent {pid}. Reason: {error_message}")

            return HttpResponse(
                content=f'Webhook received: {event["type"]} | Payment failed handled', status=200
            )
        except Exception as e:
            logger.error(f"Exception in handle_payment_intent_payment_failed:\n{traceback.format_exc()}")
            return HttpResponse(content=f'Webhook handler error: {e}', status=500)
