from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """
    Admin config for Testimonial model.

    Shows key fields in list view and provides action to approve testimonials.
    """

    list_display = ("author", "content", "created_at", "approved")
    list_filter = ("approved", "created_at")
    actions = ["approve_testimonials"]

    def approve_testimonials(self, request, queryset):
        """
        Mark selected testimonials as approved.

        Args:
            request: Current HttpRequest.
            queryset: Testimonial queryset to update.
        """
        queryset.update(approved=True)
        self.message_user(request, "Selected testimonials have been approved.")

    approve_testimonials.short_description = "Approve selected testimonials"
