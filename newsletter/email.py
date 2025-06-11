from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_newsletter_confirmation_email(email):
    subject = render_to_string(
        'newsletter/confirmation_emails/confirmation_email_subject.txt'
    ).strip()

    text_body = render_to_string(
        'newsletter/confirmation_emails/confirmation_email_body.txt',
        {'contact_email': settings.DEFAULT_FROM_EMAIL}
    )

    html_body = render_to_string(
        'newsletter/confirmation_emails/confirmation_email_body.html',
        {'contact_email': settings.DEFAULT_FROM_EMAIL}
    )

    msg = EmailMultiAlternatives(subject, text_body, settings.DEFAULT_FROM_EMAIL, [email])
    msg.attach_alternative(html_body, "text/html")
    msg.send()
