"""
URL configuration for the profiles app.

Defines URL patterns for user profile, order history,
and wishlist item removal views.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path("order_history/<order_number>", views.order_history, name="order_history"),
    path(
        "wishlist/remove/<int:item_id>/",
        views.remove_from_wishlist,
        name="remove_from_wishlist",
    ),
]
