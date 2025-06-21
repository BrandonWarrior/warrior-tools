from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonials"
    )
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Testimonial by {self.author.username} - {self.rating}/5"
