from django.http import HttpResponse
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from django.conf import settings

import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request
        stripe.api_key = settings.STRIPE_SECRET_KEY

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.get('bag')
        save_info = intent.metadata.get('save_info')

        shipping_details = intent.shipping
        grand_total = round(intent.amount_received / 100, 2)

        # Clean shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Retrieve charge to access billing_details
        try:
            charge = stripe.Charge.retrieve(intent.latest_charge)
            billing_details = charge.billing_details
            email = billing_details.email
        except Exception as e:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR retrieving charge: {e}',
                status=500
            )

        if not email:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: Missing email address',
                status=500
            )

        # Update profile info
        profile = None
        username = intent.metadata.get('username')
        if username and username != 'AnonymousUser':
            try:
                profile = UserProfile.objects.get(user__username=username)
                if save_info:
                    profile.default_full_name = shipping_details.name
                    profile.default_phone_number = shipping_details.phone
                    profile.default_country = shipping_details.address.country
                    profile.default_postcode = shipping_details.address.postal_code
                    profile.default_town_or_city = shipping_details.address.city
                    profile.default_street_address1 = shipping_details.address.line1
                    profile.default_street_address2 = shipping_details.address.line2
                    profile.default_county = shipping_details.address.state
                    profile.save()
            except UserProfile.DoesNotExist:
                pass

        # Try to find existing order
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

        # Create order if not found
        try:
            order = Order.objects.create(
                full_name=shipping_details.name,
                user_profile=profile,
                email=email,
                phone_number=shipping_details.phone,
                country=shipping_details.address.country,
                postcode=shipping_details.address.postal_code,
                town_or_city=shipping_details.address.city,
                street_address1=shipping_details.address.line1,
                street_address2=shipping_details.address.line2,
                county=shipping_details.address.state,
                grand_total=grand_total,
                original_bag=bag,
                stripe_pid=pid,
            )

            for item_id, item_data in json.loads(bag).items():
                product = Product.objects.get(id=item_id)
                if isinstance(item_data, int):
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                else:
                    for size, quantity in item_data['items_by_size'].items():
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_size=size,
                        )

        except Exception as e:
            if order:
                order.delete()
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: {e}',
                status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
