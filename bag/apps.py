"""
App configuration for the 'bag' application.
"""

from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    Configuration class for the 'bag' app.

    Sets the default primary key field type and the app name.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "bag"
