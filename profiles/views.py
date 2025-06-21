from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import UserProfile
from .forms import UserProfileForm
from products.models import WishlistItem
from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user's profile page.
    Includes delivery information form, order history, and wishlist items.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    wishlist_items = request.user.wishlist_items.select_related('product')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'wishlist_items': wishlist_items,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display the order confirmation details from a past order.
    Accessible from the user's profile page.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def remove_from_wishlist(request, item_id):
    """
    Remove a product from the user's wishlist.
    """
    try:
        item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
        item.delete()
        messages.success(request, "Item removed from your wishlist.")
    except WishlistItem.DoesNotExist:
        messages.error(request, "Item could not be found in your wishlist.")

    return HttpResponseRedirect(reverse('profile'))
