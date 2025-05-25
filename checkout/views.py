from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

def checkout(request):
    # Load Stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Retrieve user's bag
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your tool bag at the moment.")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)  # Stripe expects amount in pence (GBP)

    # Configure Stripe with secret key
    stripe.api_key = stripe_secret_key

    # Create Stripe PaymentIntent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment variables?')

    # Render the checkout template
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'bag_items': current_bag['bag_items'],
        'total': current_bag['total'],
        'delivery': current_bag['delivery'],
        'grand_total': current_bag['grand_total'],
        'product_count': current_bag['product_count'],
    }

    return render(request, template, context)
