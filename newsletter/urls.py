"""
URL patterns for the newsletter app.

Includes routes for subscribing and unsubscribing to the newsletter.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("subscribe/", views.newsletter_signup, name="newsletter_signup"),
    path("unsubscribe/", views.newsletter_unsubscribe, name="newsletter_unsubscribe"),
]
