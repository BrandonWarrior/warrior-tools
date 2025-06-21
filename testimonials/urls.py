"""
URL configuration for the testimonials app.

Defines URL patterns for creating, listing, updating, and deleting testimonials.
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        "testimonial/create/",
        views.create_testimonial,
        name="create_testimonial",
    ),
    path("list/", views.testimonial_list, name="testimonial_list"),
    path(
        "testimonial/<int:pk>/update/",
        views.update_testimonial,
        name="update_testimonial",
    ),
    path(
        "testimonial/<int:pk>/delete/",
        views.delete_testimonial,
        name="delete_testimonial",
    ),
]
