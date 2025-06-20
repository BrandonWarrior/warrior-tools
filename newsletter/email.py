from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import logging

logger = logging.getLogger("newsletter.email")


def send_newsletter_confirmation_email(email):
    """
    Send a styled HTML + plain text confirmation email to the new newsletter
    subscriber. Includes error handling and logging.
    """
    try:
        subject = render_to_string(
            "newsletter/confirmation_emails/confirmation_email_subject.txt"
        ).strip()

        text_body = render_to_string(
            "newsletter/confirmation_emails/confirmation_email_body.txt",
            {"contact_email": settings.DEFAULT_FROM_EMAIL},
        )

        html_body = render_to_string(
            "newsletter/confirmation_emails/confirmation_email_body.html",
            {"contact_email": settings.DEFAULT_FROM_EMAIL},
        )

        msg = EmailMultiAlternatives(
            subject,
            text_body,
            settings.DEFAULT_FROM_EMAIL,
            [email],
        )
        msg.attach_alternative(html_body, "text/html")
        msg.send()

    except Exception as e:
        logger.error(f"Failed to send newsletter confirmation email to {email}: {e}")


def send_unsubscribe_email(email):
    """
    Send an unsubscribe confirmation email to the user.
    """
    try:
        subject = render_to_string(
            "newsletter/unsubscribe_emails/unsubscribe_email_subject.txt"
        ).strip()

        text_body = render_to_string(
            "newsletter/unsubscribe_emails/unsubscribe_email_body.txt",
            {"contact_email": settings.DEFAULT_FROM_EMAIL},
        )

        html_body = render_to_string(
            "newsletter/unsubscribe_emails/unsubscribe_email_body.html",
            {"contact_email": settings.DEFAULT_FROM_EMAIL},
        )

        msg = EmailMultiAlternatives(
            subject,
            text_body,
            settings.DEFAULT_FROM_EMAIL,
            [email],
        )
        msg.attach_alternative(html_body, "text/html")
        msg.send()

    except Exception as e:
        logger.error(f"Failed to send unsubscribe email to {email}: {e}")
