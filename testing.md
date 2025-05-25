### 🐞 Bug Summary
product detail page displays a “size” (voltage) option for hand tools like screwdrivers, which should not have any selectable size.

Cause: 
product.has_sizes is set to True
product.variant_type is set to a value like "drill", triggering the voltage dropdown

Fix:
To resolve the issue, the product’s data was corrected by updating its attributes:
The has_sizes field was set to false to indicate the product does not require selectable sizes.
The variant_type field was cleared to prevent voltage options from being triggered by mistake.




### 🐞 Bug Summary
The "Free delivery on orders over £X!" message was not appearing in the header across the site, even though it previously worked.

Cause:
In base.html, the template was referencing {{ free_shipping_threshold }}, but the correct context variable from bag.contexts.bag_contents is free_delivery_threshold.

Fix: 
After replacing free_shipping_threshold with free_delivery_threshold, the banner now shows correctly across the site as expected.

### 🐛 Bug Summary
I was receiving a payment_intent.succeeded webhook from Stripe, but the Django webhook handler was returning a 500 error. The issue was that the code tried to access the charges property directly from the Stripe PaymentIntent object, assuming it was always present.

Cause: 
In some cases—especially in test mode or depending on the Stripe API version—charges is not included in the webhook payload. This caused an AttributeError, breaking the webhook and preventing it from processing the order.

Fix:
To make the webhook handler more reliable, I updated the code to:
First attempt to access the charges data from the webhook payload directly (which is faster and doesn't require an API call).
If charges is not available, fall back to retrieving the charge details using the latest_charge ID via the Stripe API.

