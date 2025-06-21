from django.urls import path
from . import views

"""
URL patterns for the products app.

Includes product listing, detail, add/edit/delete views, and wishlist toggle.
"""

urlpatterns = [
    path("", views.all_products, name="products"),
    path("add/", views.add_product, name="add_product"),
    path("<product_id>/", views.product_detail, name="product_detail"),
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("delete/<int:product_id>/", views.delete_product, name="delete_product"),
    path(
        "wishlist/toggle/<int:product_id>/",
        views.toggle_wishlist,
        name="toggle_wishlist",
    ),
]
