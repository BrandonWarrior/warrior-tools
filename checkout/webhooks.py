from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe
import logging

logger = logging.getLogger(__name__)


@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    stripe.api_key = settings.STRIPE_SECRET_KEY
    wh_secret = settings.STRIPE_WH_SECRET
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError as e:
        logger.error("Invalid payload: %s", e)
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
        logger.warning("Invalid signature: %s", e)
        return HttpResponse(status=400)

    except Exception as e:
        logger.exception("Unknown error during webhook construction")
        return HttpResponse(content=str(e), status=400)

    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to handler methods
    event_map = {
        "payment_intent.succeeded": handler.handle_payment_intent_succeeded,
        "payment_intent.payment_failed": handler.handle_payment_intent_payment_failed,
    }

    # Get the type of webhook from the event
    event_type = event.get("type")

    # Get the corresponding handler function or fallback to generic
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the appropriate handler function
    response = event_handler(event)
    return response
