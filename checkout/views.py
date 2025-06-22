import logging
import json

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents

import stripe

logger = logging.getLogger(__name__)


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "bag": json.dumps(request.session.get("bag", {})),
                "save_info": request.POST.get("save_info"),
                "username": (
                    request.user.username if request.user.is_authenticated else "AnonymousUser"
                ),
            },
        )
        logger.debug(f"Cached checkout data for PaymentIntent {pid}")
        return HttpResponse(status=200)
    except Exception as e:
        logger.error(f"Error caching checkout data: {e}")
        messages.error(
            request,
            "Sorry, your payment cannot be processed right now. Please try again later.",
        )
        return HttpResponse(content=str(e), status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        bag = request.session.get("bag", {})
        logger.debug(f"Checkout POST received. Bag content: {bag}")

        form_data = {
            "full_name": request.POST.get("full_name", ""),
            "email": request.POST.get("email", ""),
            "phone_number": request.POST.get("phone_number", ""),
            "country": request.POST.get("country", ""),
            "postcode": request.POST.get("postcode", ""),
            "town_or_city": request.POST.get("town_or_city", ""),
            "street_address1": request.POST.get("street_address1", ""),
            "street_address2": request.POST.get("street_address2", ""),
            "county": request.POST.get("county", ""),
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            try:
                pid = request.POST.get("client_secret").split("_secret")[0]
                logger.debug(f"Processing order with PaymentIntent id: {pid}")

                # Check if order exists already
                existing_order = Order.objects.filter(stripe_pid=pid).first()
                if existing_order:
                    logger.info(f"Order already exists for pid {pid}: {existing_order.order_number}")
                    return redirect(reverse("checkout_success", args=[existing_order.order_number]))

                order = order_form.save(commit=False)
                order.stripe_pid = pid
                order.original_bag = json.dumps(bag)

                order.save()
                logger.info(f"Order saved with order number {order.order_number}")

            except Exception as e:
                logger.error(f"Error saving order: {e}")
                messages.error(request, "Server error saving your order. Please try again.")
                return redirect(reverse("view_bag"))

            # Create order line items
            for item_id, item_data in bag.items():
                try:
                    product_id = int(item_id)
                    product = Product.objects.get(id=product_id)
                    logger.debug(f"Product found: {product.name} (id {product_id})")
                except Product.DoesNotExist:
                    logger.error(f"Product with id {item_id} not found.")
                    messages.error(
                        request,
                        "One of the products in your bag wasn't found in our database. Please call us for assistance!",
                    )
                    order.delete()
                    return redirect(reverse("view_bag"))
                except Exception as e:
                    logger.error(f"Unexpected error retrieving product {item_id}: {e}")
                    messages.error(request, "Server error. Please try again.")
                    order.delete()
                    return redirect(reverse("view_bag"))

                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                    logger.debug(f"OrderLineItem created: {product.name} x {item_data}")
                else:
                    for size, quantity in item_data.get("items_by_size", {}).items():
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_size=size,
                        )
                        order_line_item.save()
                        logger.debug(f"OrderLineItem created: {product.name} size {size} x {quantity}")

            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("checkout_success", args=[order.order_number]))
        else:
            logger.error(f"Order form invalid: {order_form.errors}")
            messages.error(
                request,
                "There was an error with your form. Please double check your information.",
            )
    else:
        bag = request.session.get("bag", {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse("products"))

        current_bag = bag_contents(request)
        total = current_bag.get("grand_total", 0)
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key

        try:
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
        except Exception as e:
            logger.error(f"Stripe PaymentIntent creation failed: {e}")
            messages.error(request, "Payment initialization failed. Please try again later.")
            return redirect(reverse("view_bag"))

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(
                    initial={
                        "full_name": profile.default_full_name,
                        "email": profile.user.email,
                        "phone_number": profile.default_phone_number,
                        "country": profile.default_country,
                        "postcode": profile.default_postcode,
                        "town_or_city": profile.default_town_or_city,
                        "street_address1": profile.default_street_address1,
                        "street_address2": profile.default_street_address2,
                        "county": profile.default_county,
                    }
                )
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(
                request,
                "Stripe public key is missing. Did you forget to set it in your environment?",
            )

        template = "checkout/checkout.html"
        context = {
            "order_form": order_form,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }

        return render(request, template, context)


def send_confirmation_email(order):
    cust_email = order.email
    subject = render_to_string(
        "checkout/confirmation_emails/confirmation_email_subject.txt",
        {"order": order},
    )
    body = render_to_string(
        "checkout/confirmation_emails/confirmation_email_body.txt",
        {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
    )
    send_mail(subject.strip(), body, settings.DEFAULT_FROM_EMAIL, [cust_email])
    logger.info(f"Confirmation email sent to {cust_email}")


def checkout_success(request, order_number):
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                "default_full_name": order.full_name,
                "default_phone_number": order.phone_number,
                "default_country": order.country,
                "default_postcode": order.postcode,
                "default_town_or_city": order.town_or_city,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_county": order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
                logger.debug(f"User profile updated for {request.user.username}")

    messages.success(
        request,
        (
            f"Order successfully processed! Your order number is {order_number}. "
            f"A confirmation email will be sent to {order.email}."
        ),
    )

    if "bag" in request.session:
        del request.session["bag"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    send_confirmation_email(order)

    return render(request, template, context)
