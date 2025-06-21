from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """
    Custom ModelAdmin for the Testimonial model.

    Displays key fields in the list view and provides an action to approve
    selected testimonials.
    """

    list_display = ("author", "content", "created_at", "approved")
    list_filter = ("approved", "created_at")
    actions = ["approve_testimonials"]

    def approve_testimonials(self, request, queryset):
        """
        Approves selected testimonials by setting their approved field to True.

        Args:
            request: The current HttpRequest object.
            queryset: A QuerySet of Testimonial instances to be approved.
        """
        queryset.update(approved=True)
        self.message_user(request, "Selected testimonials have been approved.")

    approve_testimonials.short_description = "Approve selected testimonials"
