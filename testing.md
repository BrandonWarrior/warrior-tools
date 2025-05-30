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

### 🐛 Bug Summary
While working on my Django Stripe integration, I encountered a persistent HTTP 500 error triggered by the payment_intent.succeeded webhook from Stripe. It turned out to be caused by assumptions I made in the webhook handler.

Cause:
The webhook handler was trying to access billing_details.email directly from intent.charges.data[0], but in some cases, that field wasn’t present in the webhook payload. When that happened, the code threw an AttributeError or failed due to a missing required field (email) for order creation.

I also didn’t have proper fallback logic in place to retrieve the email from other possible sources, like intent.receipt_email, nor did I safeguard against missing charges.

Fix:
To resolve the issue, I added robust fallback logic in the webhook handler to check if charges exist and safely pull the email address. If the billing email is missing, it now falls back to receipt_email. I also added a guard clause to return a clean error response if an email still isn’t found, avoiding a crash. This fixed the 500 error, and Stripe webhooks are now being handled successfully.

### 🐞 Bug Summary
The “Wrenches & Pliers” category did not display any products when selected from the Hand Tools dropdown menu, even though products existed and showed up via search.

Cause:
The dropdown link was using an outdated category query string:
?category=wrenches
However, the actual category name (slug) in the database was updated to wrenches_and_pliers, resulting in no match and an empty product list.

Fix:
The dropdown link was corrected to use the updated category slug:
The link in main-nav.html was changed from ?category=wrenches to ?category=wrenches_and_pliers.
The combined “All Hand Tools” link was also updated to include wrenches_and_pliers in the list of categories.

