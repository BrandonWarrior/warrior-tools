from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignupForm
from .models import NewsletterSubscriber
from .email import send_newsletter_confirmation_email

def newsletter_signup(request):
    """
    Display and process the newsletter signup form.
    Sends confirmation email upon successful subscription.
    """
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            send_newsletter_confirmation_email(subscriber.email)
            messages.success(request, 'Thanks for subscribing to the Warrior Tools Newsletter!')
            return redirect('newsletter_signup')
    else:
        form = NewsletterSignupForm()

    return render(request, 'newsletter/newsletter_signup.html', {'form': form})


def newsletter_unsubscribe(request):
    """
    Allow users to unsubscribe from the newsletter by submitting their email.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            subscriber = NewsletterSubscriber.objects.get(email=email)
            subscriber.delete()
            messages.success(request, "You've been unsubscribed from the Warrior Tools Newsletter.")
        except NewsletterSubscriber.DoesNotExist:
            messages.error(request, "That email is not subscribed.")
        return redirect('newsletter_unsubscribe')

    return render(request, 'newsletter/unsubscribe.html')
