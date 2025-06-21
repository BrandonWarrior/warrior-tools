from django import forms
from .models import NewsletterSubscriber


class NewsletterSignupForm(forms.ModelForm):
    """
    Form for signing up a user to the newsletter with an email field.
    """
    class Meta:
        model = NewsletterSubscriber
        fields = ["email"]
