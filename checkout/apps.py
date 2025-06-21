"""
App configuration for the checkout app.

Sets up the CheckoutConfig class and imports
signals on app ready.
"""

from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration for the 'checkout' application.

    Sets the default auto field and imports signal
    handlers when the app is ready.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "checkout"

    def ready(self):
        """
        Import signal handlers for the checkout app.

        Ensures signal receivers are registered when
        the app is ready.
        """
        import checkout.signals
