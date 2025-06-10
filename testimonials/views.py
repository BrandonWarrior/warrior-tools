from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm
from .models import Testimonial

@login_required
def create_testimonial(request):
    """
    Handles testimonial creation with standard form submission.
    """
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.author = request.user
            testimonial.save()
            messages.success(request, "Your testimonial has been submitted for approval!")
            return redirect('testimonial_list')
        else:
            messages.error(request, "There was an error submitting your testimonial.")
    else:
        form = TestimonialForm()

    return render(request, 'testimonials/create_testimonial.html', {'form': form})

def testimonial_list(request):
    """
    Displays approved testimonials.
    """
    testimonials = Testimonial.objects.filter(approved=True).order_by('-created_at')
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})
