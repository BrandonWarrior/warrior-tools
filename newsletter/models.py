from django.db import models

"""
Models for the newsletter app.
"""


class NewsletterSubscriber(models.Model):
    """
    Represents a subscriber to the newsletter identified by a unique email.
    Records the date when the subscription was created.
    """
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
