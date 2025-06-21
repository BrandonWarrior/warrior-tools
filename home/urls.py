"""
URL configuration for the Home app.
Defines the URL pattern for the home page.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
]
