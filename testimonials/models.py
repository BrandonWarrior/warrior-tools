from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):
    """
    Model representing a user testimonial.

    Attributes:
        author (ForeignKey): Reference to the User who authored the testimonial.
        content (TextField): The content of the testimonial.
        rating (IntegerField): Rating from 1 to 5, default is 5.
        created_at (DateTimeField): Timestamp of testimonial creation.
        approved (BooleanField): Whether the testimonial is approved for display.
    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonials"
    )
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Testimonial by {self.author.username} - {self.rating}/5"
