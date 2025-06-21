from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm
from .models import Testimonial


@login_required
def create_testimonial(request):
    """
    Handle testimonial creation.
    """
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.author = request.user
            testimonial.save()
            messages.success(
                request, "Your testimonial has been submitted for approval!"
            )
            return redirect("testimonial_list")
        else:
            messages.error(request, "There was an error submitting your testimonial.")
    else:
        form = TestimonialForm()

    return render(request, "testimonials/create_testimonial.html", {"form": form})


def testimonial_list(request):
    """
    Display a list of approved testimonials.
    """
    testimonials = Testimonial.objects.filter(approved=True).order_by("-created_at")

    return render(
        request, "testimonials/testimonial_list.html", {"testimonials": testimonials}
    )


@login_required
def update_testimonial(request, pk):
    """
    Allow a user to update their own testimonial.
    Resets approval status so it must be reviewed again by admin.
    """
    testimonial = get_object_or_404(Testimonial, pk=pk, author=request.user)

    if request.method == "POST":
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.approved = False  # Unapprove on edit
            testimonial.save()
            messages.success(
                request, "Your testimonial has been updated and is pending approval."
            )
            return redirect("testimonial_list")
    else:
        form = TestimonialForm(instance=testimonial)

    return render(request, "testimonials/update_testimonial.html", {"form": form})


@login_required
def delete_testimonial(request, pk):
    """
    Allow a user to delete their own testimonial.
    """
    testimonial = get_object_or_404(Testimonial, pk=pk, author=request.user)

    if request.method == "POST":
        testimonial.delete()
        messages.success(request, "Your testimonial has been deleted.")
        return redirect("testimonial_list")

    return render(
        request, "testimonials/delete_testimonial.html", {"testimonial": testimonial}
    )
