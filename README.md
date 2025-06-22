# Warrior Tools


## 📄 Additional Documentation

  [📑 Planning & User Stories](PLANNING.md)

  [🧪 Testing & Validation](TESTING.md)

## Overview
Warrior Tools is an e-commerce website designed to serve construction professionals and DIY enthusiasts with a curated selection of high-quality tools. This project brings together my real-world experience in the construction industry and the technical skills I've gained during my time at the Code Institute.

As someone currently working in construction, tools aren't just products to me—they're essential, everyday companions on the job. I wanted to create a platform that not only showcases the tools I know and trust, but also demonstrates how practical, hands-on knowledge can be translated into a functional and user-friendly web application.

Building Warrior Tools allowed me to fuse my passion for construction with my growing skills in web development, resulting in a website that feels authentic, useful, and personal. From the product pages to the checkout experience, every part of the site was built with both the user and the tradesperson in mind.

## 🏢 Business Type

Warrior Tools currently operates as a B2C (Business to Consumer) e-commerce platform, catering to individuals working in construction, trades, and DIY markets. The platform is designed to provide:

- High-quality, trusted tool brands

- A user-friendly interface for quick and secure purchasing

- Efficient navigation and product filtering for professionals on the go

While the site is presently geared toward individual consumers, it is built with scalability in mind. There is a clear roadmap for evolving Warrior Tools into a B2B (Business to Business) model—serving construction firms, contractors, and trade suppliers with bulk ordering, trade accounts, and personalized procurement solutions.

This future adaptability makes Warrior Tools not just a final project, but the foundation of a real, scalable business opportunity.

## 📈 Content Planning & SEO Strategy
To ensure Warrior Tools reaches its intended audience effectively, the site’s content, layout, and metadata have been thoughtfully designed with both user engagement and search engine optimization (SEO) in mind.

### 🏠 Welcome Message (Hero Section)
WARRIOR TOOLS is your trusted online store for power tools, hand tools, and accessories. We offer a curated selection of high-quality tools for professionals and DIY enthusiasts, backed by excellent customer service and fast UK delivery.

This message immediately conveys trust, relevance, and targeted keywords to improve visibility on search engines and reassure visitors of the site's value proposition.

## 🎯 Target Audience
Warrior Tools is built for:

- 🧰 Professional builders and contractors who rely on durable, trusted equipment

- 🛠️ DIY enthusiasts and home renovators seeking quality tools for personal projects

- 👷 Trade apprentices and tool collectors looking for affordable, entry-level gear

By tailoring both content and design to these audiences, the site ensures a relevant, intuitive experience for every visitor.

## 📢 Content Strategy
To build trust and provide value to users, the site incorporates:

product descriptions with technical specifications

Clear calls to action (e.g., Add to Bag, Product Details, Sign Up)

Streamlined user flows for both browsing and checkout

## 🎨 Colour Palette
The Warrior Tools site uses a strong, consistent colour scheme to reinforce its professional, trustworthy identity. Here’s a breakdown of the main colours used:

| Colour Name           | Hex Code                          | Usage Description                                   |
| --------------------- | --------------------------------- | --------------------------------------------------- |
| **Navy Blue**         | `#1A4C8C`                         | Primary brand colour: buttons, headings, borders    |
| **Dark Navy**         | `#0B0F1A`                         | Backgrounds for navbar, footer, and call-to-actions |
| **Dark Blue Hover**   | `#163f73`                         | Hover states for buttons and links                  |
| **White**             | `#ffffff`                         | Background, text, buttons for contrast              |
| **Muted Grey**        | `#6c757d`                         | Placeholder text, subtle accents                    |
| **Light Grey Border** | `#dee2e6`                         | Divider and border colour for cards and containers  |
| **Gold/Amber**        | `#ffc107`                         | Alerts, star ratings, focus outlines                |
| **Green**             | `#1e7e34` / `#218838` / `#28a745` | Success indicators, CTA buttons, toast headers      |
| **Red**               | `#dc3545` / `#c82333`             | Used for remove/delete warnings                     |
| **Text Default**      | `#333`                            | Main body text                                      |


## Screenshots
## 📸 Screenshots

### Home Pages
- [Home](docs/screenshots/home.png)
- [Home 2](docs/screenshots/home2.png)

Screenshots showing the homepage designs and layout variations users first see.

### Products
- [Product Detail](docs/screenshots/product-detail.png)
- [Products](docs/screenshots/products.png)

Views of product listings and detailed product pages highlighting tool information.

### Product Management
- [Add Product](docs/screenshots/add-product.png)
- [Add Product Test](docs/screenshots/add-product-test.png)
- [Add Product 2](docs/screenshots/add-product2.png)
- [Add Product 3](docs/screenshots/add-product3.png)
- [Edit Product](docs/screenshots/edit-product.png)
- [Edit Product 2](docs/screenshots/edit-product2.png)

Admin interface screenshots for adding and editing products in the inventory.

### Shopping Bag
- [Bag](docs/screenshots/bag.png)

Displays the shopping cart interface where users review selected items before checkout.

### Checkout
- [Checkout](docs/screenshots/checkout.png)
- [Checkout 2](docs/screenshots/checkout2.png)

Checkout pages illustrating payment and shipping forms users complete to place orders.

### Orders
- [Order Confirmed](docs/screenshots/order-confirmed.png)

Confirmation page after successful order placement with order details and summary.

### Navigation, Header and Footer
- [Desktop Header](docs/screenshots/desktop-header.png)
- [Header Nav](docs/screenshots/header-nav.png)
- [My Account Dropdown](docs/screenshots/my-account-dropdown.png)
- [Smaller Header](docs/screenshots/smaller-header.png)
- [Smaller Nav](docs/screenshots/smaller-nav.png)
- [Footer](docs/screenshots/footer.png)

Various navigation bars, menus, dropdowns, and header/footer elements across pages.


### Profile
- [Profile](docs/screenshots/profile.png)

User profile dashboard showing saved delivery info, past orders, and wishlist access.

### Wishlist
- [Wishlist](docs/screenshots/wishlist.png)

User’s wishlist page with saved tools for future purchase consideration.

### Newsletter
- [Newsletter](docs/screenshots/newsletter.png)
- [Newsletter Validation](docs/screenshots/newsletter-val.png)

Newsletter subscription forms and validation messages shown to site visitors.

### Testimonials
- [Submit Testimonial](docs/screenshots/submit-testimonial.png)
- [Testimonial Validation](docs/screenshots/testimonial-val.png)

User-submitted feedback forms and admin validation screens for reviews.

### Toast Notifications
- [Tool Added Toast](docs/screenshots/too-added-toast.png)
- [Order Confirmed Toast](docs/screenshots/order-confirmed-toast.png)
- [Testimonial Toast](docs/screenshots/testimonial-toast.png)

Popup notification examples confirming actions like adding tools or order success.

### Admin
- [Admin](docs/screenshots/admin.png)

Django admin panel screenshots showing product and testimonial management.

## ✨ Key Features at a Glance

- Full e-commerce shopping cart with Stripe integration
- Secure user authentication with profile management
- Dynamic product filtering and variant options
- Wishlist and testimonial features for engagement
- Newsletter signup and email verification
- AWS S3 storage for scalability

## 🧩 Custom Models & Apps

### 🧩 home App
The home app manages the site’s landing page and any general-purpose static pages (e.g., About, Contact). It provides users with a first impression and sets the tone for the brand.

#### 📄 views.py
index(request)

Renders the homepage template (index.html)

Does not contain dynamic logic — simply returns the main entry point to the site

#### 📄 models.py
Empty — this app does not use any database models, as it's purely for static/static-like content

#### 📄 urls.py
Maps the root URL (/) to the index view

May also include other static routes like /about/ or /contact/ if added

#### 📄 admin.py
Empty (or default) — no models to register

#### 📄 apps.py
Default app configuration generated by Django

#### 📝 Summary
The home app serves as the user’s first interaction with Warrior Tools. It renders static pages and sets up the structure for marketing content. Its simplicity and separation from business logic ensure clean routing and maintainability.

### products App
The products app is responsible for displaying, filtering, and managing the tools available on the Warrior Tools eCommerce platform.

#### 🔍 models.py
This file defines two key models:

Category

Stores product categories with a name and optional friendly_name for display.

Includes a custom plural name ("Categories") and a helper method get_friendly_name().

Product

Represents each tool with fields like name, sku, description, price, rating, and image.

Supports optional size selection via has_sizes.

Categorizes products using a ForeignKey to Category.

Defines VARIANT_CHOICES (e.g., hammer, jigsaw, orbital sander) to help distinguish product types.

#### 📄 views.py
This file contains the main logic for product display and search functionality:

all_products(request)

Displays all products with optional filtering by category, search term, and sorting (e.g., name or category).

Supports GET parameters:

sort (e.g., name, category)

direction (asc, desc)

q (search query)

category (comma-separated filter)

Other views (not fully shown in preview) likely include:

Individual product detail display

Admin-only product management (if applicable)

#### 🧾 Other Files
forms.py – Manages forms for creating/editing products (via ProductForm)

admin.py – Registers Product and Category in the Django admin

urls.py – Maps URLs like /products/ and /products/<product_id>/ to view functions

### 🧩 bag App
The bag app handles all functionality related to the shopping cart (referred to as the "bag" on the site).

#### 📄 models.py
This file is intentionally empty. The cart does not persist to the database but instead uses Django sessions to store items temporarily until checkout.

#### 📄 views.py
This file contains key view functions for shopping cart behavior:

view_bag(request)
Renders the shopping bag page showing all current items stored in the session.

add_to_bag(request, item_id)
Adds a product to the session-based bag, with logic to:

Handle items with or without sizes

Update quantities if an item already exists

Store items using nested dictionaries under the session key "bag"

adjust_bag(request, item_id) (not in preview but expected)
Adjusts the quantity of a product already in the bag.

remove_from_bag(request, item_id) (expected)
Removes a product from the session cart entirely.

#### 🧠 Additional Logic
contexts.py
Provides a context processor that makes bag contents and totals available across all templates. This is essential for rendering the cart icon/total in the navbar.

templatetags/
May include custom template filters (if implemented) to assist with bag rendering.

#### 🧾 Summary
This app is a self-contained module that leverages session storage for cart logic. It's an example of lightweight, scalable design for managing transient user data without the overhead of database models.

### 🧩 checkout App
The checkout app manages the full order processing flow, including collecting shipping information, calculating totals, and integrating with Stripe for secure payments.

#### 📄 models.py
Two main models are defined:

Order

Stores all key information for a customer order including:

Contact details (full_name, email, phone_number)

Shipping information (country, postcode, address)

Order metadata (date, delivery cost, total, grand total)

Reference to the logged-in user via a ForeignKey to UserProfile

Automatically assigns a unique order_number using UUID

Contains helper methods to update the order total and calculate grand total dynamically

OrderLineItem (just beyond preview, but typically included)

Linked to the Order via a ForeignKey

Stores individual product, quantity, line item total, and optional size variant

Together, these models form the backbone of the order tracking and checkout pipeline.

### 🧩 profiles App
The profiles app handles user-specific data and settings. It allows authenticated users to:

View and update their saved delivery information

See past orders

Manage wishlist items

It integrates closely with the checkout, products, and Django User models.

#### 📄 models.py
UserProfile

One-to-one relationship with Django’s User model

Stores default delivery info (name, phone, address, country)

Signal:

A @receiver(post_save) function listens for changes to the User model:

Automatically creates a UserProfile when a new user is registered

Updates the profile if an existing User is saved

This logic is built directly into models.py, so there is no separate signals.py file in this app.

#### 📄 views.py
profile(request)

Displays and processes the profile form

Pre-fills with existing delivery info from the UserProfile

Also fetches:

Related orders (profile.orders.all())

Wishlist items (request.user.wishlist_items)

order_history(request, order_number)

Allows users to view past order details from their profile

Reuses the checkout success template to show full order breakdown

#### 📄 forms.py
Defines the UserProfileForm

Allows users to update name, address, phone number, and country

Used in the profile view for both GET and POST requests

#### 📄 urls.py
Routes user requests to:

/profile/ → Profile view

/profile/orders/<order_number>/ → Order history detail view

#### 📄 admin.py
Registers UserProfile with the Django admin site

Useful for backend review of user delivery settings

#### 📝 Summary
The profiles app extends Django's user model to support a personalised shopping experience. By storing default delivery information and linking to past orders and wishlist items, it streamlines the checkout process and offers users a centralized profile dashboard. Core functionality is delivered through a combination of views, a form, and a signal—all working together to maintain an up-to-date user profile automatically.

### 🧩 newsletter App
The newsletter app manages email subscriptions from site visitors who want to receive updates, new tool announcements, and helpful usage tips in the future.

It provides a simple but scalable foundation for email marketing.

#### 📄 models.py
NewsletterSubscriber

Stores the email address of each subscriber (enforced as unique)

Automatically records the subscription timestamp using date_joined

Provides a string representation returning the subscriber’s email

#### 📄 views.py
Handles:

Display and submission of the newsletter signup form

Success and error feedback using Django messages

#### 📄 forms.py
Defines a simple form (NewsletterForm) to collect a single EmailField

Validates that the email is not already subscribed

#### 📄 email.py
Likely handles custom email logic (e.g., sending a welcome message or preparing future campaigns)

Can be integrated with services like SendGrid or Mailchimp in the future

#### 📄 urls.py
Maps routes like /newsletter/subscribe/ to the appropriate view

#### 📄 admin.py
Registers NewsletterSubscriber so subscriptions can be viewed or managed via the Django admin panel

#### 📝 Summary
The newsletter app enables users to subscribe to email updates. It is designed with simplicity and extendibility in mind—ready to be paired with email delivery services for future campaigns. It uses clean models, a reusable form, and straightforward views to integrate with any section of the site (e.g., homepage footer or modal pop-up).

### 🧩 testimonials App
The testimonials app allows users to submit reviews or feedback about the site, which can then be reviewed and published by an admin. This builds trust and social proof for potential customers.

### 📄 models.py
Testimonial

Stores individual testimonials with the following fields:

author: ForeignKey to User

content: The user-submitted feedback text

rating: Integer from 1 to 5 (with dropdown choices)

created_at: Timestamp of when the testimonial was submitted

approved: Boolean to control whether it’s published

Only approved testimonials should be displayed on the front end.

### 📄 views.py
Manages:

Displaying approved testimonials

Handling testimonial submission by authenticated users

Likely includes a view to thank the user or confirm submission

### 📄 forms.py
Defines a form for users to submit:

Rating

Feedback content

Includes basic validation to ensure proper input format and optional custom error messages.

### 📄 urls.py
Maps URLs like /testimonials/ and /testimonials/submit/ to the respective views

### 📄 admin.py
Registers the Testimonial model

Enables staff to approve or reject submissions before they go live

### 📝 Summary
The testimonials app gives users a voice and provides potential customers with authentic reviews. Featuring moderation tools for admins and a clean model-view-form pattern, it enhances both credibility and user engagement on the site.

## 💳 Stripe Payment Integration
Stripe is used to securely handle payment processing on the Warrior Tools website. It enables customers to make real-time payments using debit or credit cards with confidence.

### 🔐 Why Stripe?
PCI-compliant and secure by design

No sensitive card data stored on the site

Simple integration via JavaScript and Django backend

Allows real-time validation and error handling

### ⚙️ How Stripe Is Integrated
Frontend (JS & HTML):

Stripe’s JavaScript SDK is used to capture payment details securely.

A custom checkout form is rendered using Stripe Elements (in checkout/templates/checkout/checkout.html).

Real-time card validation and error messages are handled client-side.

Backend (Django):

On form submission, a Stripe PaymentIntent is created via Stripe’s Python SDK.

The client_secret is returned to the frontend to complete the transaction.

Metadata (such as the contents of the cart and the user info) is attached to the PaymentIntent via the cache_checkout_data view.

Webhooks:

The webhooks.py and webhook_handler.py files listen for payment success or failure events.

When a payment_intent.succeeded webhook is received:

An order is finalized in the database.

A confirmation email is sent to the user.

The cart is cleared from the session.

### 🧪 Testing Stripe in Dev Mode
Test card number for development:

Card Number: 4242 4242 4242 4242

Expiry: Any future date

CVC: Any 3-digit number

Postal Code: Any value

Stripe is currently running in test mode, with live keys to be added before production.

## ☁️ AWS S3 & Media File Storage
Warrior Tools uses Amazon Web Services (AWS) — specifically S3 (Simple Storage Service) — to manage and serve static and media files in a production environment.

This ensures scalability, reliability, and fast delivery of assets like product images, CSS, and JavaScript.

### 🔧 What AWS Services Are Used
Amazon S3

Stores and serves static files (CSS, JS) and user-uploaded media (e.g. product images)

Configured with two buckets:

One for static files (pre-collected via collectstatic)

One for media files (uploaded by admins or users)

Buckets are made public-read for safe, direct browser access

AWS IAM (Identity & Access Management)

A dedicated IAM user was created for this project

Permissions restricted to only allow access to the S3 buckets

Access and secret keys stored securely in env.py and on Heroku as config vars

AWS CloudFront (optional enhancement)

Can be used for CDN delivery if project scales further

### ⚙️ Django Configuration
custom_storages.py

Defines two storage backends:

StaticStorage: For static files

MediaStorage: For uploaded media

These are referenced in settings.py using:

python
Copy code
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
boto3 and django-storages

Installed via requirements.txt

Handle file upload and retrieval to/from S3 programmatically

### 🔐 Security Considerations
AWS credentials are never committed to Git — they are stored in env.py and Heroku config vars

S3 buckets use strict permissions with no public write access

Media URLs are safely served via S3 links, reducing load on the Heroku dyno

### 🧪 Local vs Production
Local Development:

Uses Django’s default static and media storage on the local file system

Production (Heroku + AWS):

Automatically switches to S3 for file handling using environment variables

## 📧 Email Integration
Warrior Tools uses email in three key areas to keep users informed and secure:

Order confirmations after checkout

Newsletter subscriptions and unsubscriptions

Account registration email verification

These emails are handled using Django’s send_mail() function, secure SMTP backend, and context-driven templates.

### 🛒 1. Order Confirmation Emails
Triggered automatically after successful payment via Stripe.

Includes:

Order reference

Product summary

Delivery address

Templates:

confirmation_email_subject.txt

confirmation_email_body.txt

### 📨 2. Newsletter Subscription Emails
✅ On Subscription:

User email is added to NewsletterSubscriber model

Sends a welcome/confirmation email outlining:

What they’ll receive (e.g., new tool announcements, usage tips)

❌ On Unsubscription:

Email is deleted from the system

A confirmation email is sent to notify the user they’ve successfully unsubscribed

### 🔑 3. Email Verification on Signup
When a new user registers, a verification email is sent.

The email includes a unique activation link.

The account remains inactive until the user verifies their email via the link.

This helps:

Prevent spam/bot signups

Confirm user identity

Ensure email deliverability for order receipts

Note: If you’re using packages like django-allauth or a custom token system, mention it here.

### ⚙️ Technical Details
SMTP via Gmail or compatible service

Email settings securely loaded from environment variables:

python
Copy code
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
Local testing uses Django’s console.EmailBackend

Production delivery confirmed with real inboxes

### 🧪 Testing Summary
All email flows tested manually:

Order confirmation

Newsletter subscribe/unsubscribe

Email verification on account signup

Confirmed email content is rendered correctly with user-specific data

Invalid email scenarios handled gracefully

## 🔐 Environment Variables & Security
Warrior Tools follows security best practices by separating sensitive configuration data from the codebase using environment variables. This approach protects secret keys, credentials, and tokens from being exposed in version control or the public domain.

### 📁 env.py for Local Development
A local env.py file is used to store all sensitive keys and configuration values. This file is excluded from version control using .gitignore.

Sample structure of env.py:

python
Copy code
import os

os.environ["SECRET_KEY"] = "your-secret-django-key"
os.environ["STRIPE_PUBLIC_KEY"] = "your-test-stripe-public-key"
os.environ["STRIPE_SECRET_KEY"] = "your-test-stripe-secret-key"
os.environ["STRIPE_WH_SECRET"] = "your-stripe-webhook-secret"
os.environ["EMAIL_HOST_USER"] = "your-email@gmail.com"
os.environ["EMAIL_HOST_PASS"] = "your-app-password"
os.environ["AWS_ACCESS_KEY_ID"] = "your-aws-key"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your-aws-secret"
os.environ["DATABASE_URL"] = "your-postgres-url"
☁️ Heroku Configuration
In production, all of these values are set securely in the Heroku Config Vars section (under Settings → Reveal Config Vars). This includes:

SECRET_KEY

STRIPE_PUBLIC_KEY

STRIPE_SECRET_KEY

STRIPE_WH_SECRET

EMAIL_HOST_USER

EMAIL_HOST_PASS

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

USE_AWS (a custom flag to enable AWS S3 in production)

DATABASE_URL (Heroku's PostgreSQL database URL)

These are accessed in settings.py using:

python
Copy code
import os

SECRET_KEY = os.environ.get("SECRET_KEY")
🔒 Git Ignore & Security Measures
The following files and directories are explicitly excluded from Git via .gitignore:

env.py

.env (if used)

.venv/

Any local DB or system-specific files

Credentials and access keys are never hardcoded into the codebase or templates.

### Summary
Using environment variables ensures Warrior Tools is secure, portable, and production-ready. It separates code from configuration, allows safe deployment via Heroku, and supports secret rotation and CI/CD practices.

## 🚀 Heroku Deployment
Warrior Tools is deployed using Heroku, a cloud-based platform that supports Django projects with PostgreSQL, automatic scaling, and environment variable management.

### 🔧 Tools Used
Heroku – App hosting

Heroku Postgres – Live production database

AWS S3 – For static/media file storage (see AWS section)

Stripe – Payment processing (via keys in config vars)

Gunicorn – Production-ready WSGI HTTP server

Whitenoise – Local static file serving during dev/testing (optional)

### 📦 Deployment Steps
Prepare Requirements & Config Files

Ensure requirements.txt is up to date:

bash
Copy code
pip freeze > requirements.txt
Add Procfile with:

makefile
Copy code
web: gunicorn warrior_tools.wsgi
Add runtime.txt to specify Python version (e.g., python-3.11.9)

Commit & Push to GitHub

All project code must be in a GitHub repo (e.g., BrandonWarrior/warrior-tools)

Create the Heroku App

Via Heroku CLI or Dashboard:

bash
Copy code
heroku create your-app-name
Set Buildpacks

Python (auto-detected)

Add Heroku Postgres from the Resources tab

Configure Environment Variables

In Heroku Dashboard > Settings > Config Vars, add:

SECRET_KEY

DEBUG = False

ALLOWED_HOSTS = your-app.herokuapp.com

DATABASE_URL

USE_AWS = True

Stripe, AWS, and email-related variables (see Environment Variables)

Deploy Code

Use Git:

bash
Copy code
git push heroku main
Database Migration

bash
Copy code
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
Collect Static Files

bash
Copy code
heroku run python manage.py collectstatic
### 🔍 Post-Deployment Checklist
✅ Site loads correctly at https://your-app.herokuapp.com/

✅ Admin panel accessible at /admin/

✅ Stripe test checkout functions correctly

✅ Newsletter and confirmation emails send successfully

✅ Static and media files load via AWS S3

## 🚧 Future Enhancements

As Warrior Tools evolves beyond the scope of this project, several additional features are being considered to improve user experience, support business scalability, and offer greater value to tradespeople and DIY customers alike.

### ⭐ Product Reviews & Ratings
Enable users to leave detailed reviews and star ratings on products they’ve purchased. This would help build trust and aid other users in making informed buying decisions. Admin moderation could be included to ensure quality control.

### 🛠️ Trade Accounts (B2B Support)
Introduce a dedicated login flow for trade customers such as construction firms or contractors. Features could include:
- Bulk purchasing
- Custom trade pricing
- Invoicing
- Repeat order functionality
This would support Warrior Tools' shift from B2C to B2B commerce.

### 🧾 Downloadable Invoices
Allow logged-in users to download PDF invoices from their profile or order history pages. This would help both professionals and businesses keep accurate records for tax or expense purposes.

### 📰 Blog & Tool Tips Section
Launch a blog or tips area to share:
- Tool care and maintenance advice
- Product comparisons
- DIY project inspiration
This would drive SEO while also providing value-added content for subscribed users.

### 💬 Live Chat Support
Integrate a live chat widget (e.g., Tawk.to or Intercom) for real-time assistance with:
- Product enquiries
- Delivery questions
- Checkout issues
It would enhance the user support experience and reduce bounce rates.

### 🎯 Personalised Recommendations
Use browsing history or past purchases to recommend tools or accessories tailored to each user’s preferences or trade.

### 📦 Enhanced Product Variants
Extend support for product variants (e.g., sizes, colours, power types). This would improve product data handling and provide greater flexibility for inventory listings.

### 🛡️ Multi-Factor Authentication
Add extra security for user accounts by enabling multi-factor authentication (MFA), particularly for admin logins or trade users.

### 🌍 International Shipping Support
Build in support for international delivery options with:
- Country-specific pricing
- Currency conversion
- Estimated shipping times

### 📈 Reporting Dashboard (Admin)
Create an admin-only analytics dashboard to display:
- Sales metrics
- Popular products
- Stock levels
This would support decision-making and business scaling.

## 🙏 Credits

### 🎓 Project Guidance & Educational Support
- [Code Institute](https://codeinstitute.net/) — for the comprehensive project walkthrough, structure guidance, and technical mentoring during the development of Warrior Tools.

---

### ✍️ Feature Inspirations
The following features have been planned or partially implemented for future development. Each is inspired or informed by specific tutorials or documentation relevant to Django-based development.

| **Feature**                        | **Source & Link**                                                                                                                                                                                                                                                 | **Relevance to Project**                                                                                |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Wishlist Functionality**         | [TutorialsPoint – Simple Wishlist App Using Django](https://www.tutorialspoint.com/django/simple-wishlist-app-using-django.htm)<br>[Django-Oscar Wishlist Docs](https://django-oscar.readthedocs.io/en/latest/topics/wishlists.html)                              | Helped structure the `Wishlist` model linking users and products, with views for adding/removing items. |
| **Newsletter Signup & Management** | [Dev.to – Build an Email Newsletter Subscriber in Django](https://dev.to/silvinodias/how-to-build-an-email-newsletter-subscriber-in-django-49de)<br>[Twilio SendGrid – Email Newsletter in Django](https://docs.sendgrid.com/for-developers/sending-email/django) | Guided creation of the subscriber model, signup form, and email confirmation flow using SendGrid.       |
| **Testimonials & Feedback System** | [Code4Startup – Create a Testimonial Page in Django](https://code4startup.com/projects/testimonial-page-in-django)                                                                                                                                                | Inspired the Testimonial model with admin approval, star ratings, and frontend display logic.           |

---

### 🛠️ Open‑Source Libraries & Tools

- [Django](https://www.djangoproject.com/) — framework for structuring the backend and core logic  
- [Stripe](https://stripe.com/) — secure payment gateway integration  
- [AWS S3 / django-storages](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) — used for serving media and static files in production  
- [Bootstrap](https://getbootstrap.com/), [FontAwesome](https://fontawesome.com/), [Google Fonts](https://fonts.google.com/) — for responsive, accessible, and visually clean front-end design

- Black — code formatter used to enforce consistent style with a line length of 88 characters

- Flake8 — linting tool to ensure PEP8 compliance and catch code quality issues
