"""
App configuration for the profiles application.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration class for the profiles app.
    Sets default auto field type and app name.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"
