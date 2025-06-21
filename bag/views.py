"""
Views for managing the shopping bag.

Includes views to display bag contents, add items, adjust quantities,
and remove items from the bag.
"""

from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """
    Render the shopping bag contents page.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered bag contents page.
    """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """
    Add a quantity of a specified product to the shopping bag.

    Handles products with and without sizes.

    Args:
        request (HttpRequest): The incoming HTTP request.
        item_id (str): ID of the product to add.

    Returns:
        HttpResponseRedirect: Redirect to the provided URL after adding.
    """
    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = request.POST.get("product_size")
    item_id = str(item_id)
    bag = request.session.get("bag", {})

    if size:
        if item_id in bag:
            if isinstance(bag[item_id], dict) and "items_by_size" in bag[item_id]:
                if size in bag[item_id]["items_by_size"]:
                    bag[item_id]["items_by_size"][size] += quantity
                    new_qty = bag[item_id]["items_by_size"][size]
                    messages.success(
                        request,
                        f"Updated {size.upper()} {product.name} quantity to {new_qty}",
                    )
                else:
                    bag[item_id]["items_by_size"][size] = quantity
                    messages.success(
                        request,
                        f"Added {size.upper()} {product.name} to your bag",
                    )
            else:
                bag[item_id] = {"items_by_size": {size: quantity}}
                messages.success(
                    request,
                    f"Added {size.upper()} {product.name} to your bag",
                )
        else:
            bag[item_id] = {"items_by_size": {size: quantity}}
            messages.success(
                request,
                f"Added {size.upper()} {product.name} to your bag",
            )
    else:
        if item_id in bag and isinstance(bag[item_id], int):
            bag[item_id] += quantity
            messages.success(
                request,
                f"Updated {product.name} quantity to {bag[item_id]}",
            )
        else:
            bag[item_id] = quantity
            messages.success(
                request,
                f"Added {product.name} to your bag",
            )

    request.session["bag"] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of a specified product in the bag.

    Handles removal if quantity is zero or less.

    Args:
        request (HttpRequest): The incoming HTTP request.
        item_id (str): ID of the product to adjust.

    Returns:
        HttpResponseRedirect: Redirects to the bag view page.
    """
    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get("quantity"))
    size = request.POST.get("product_size")
    item_id = str(item_id)
    bag = request.session.get("bag", {})

    if size:
        if quantity > 0:
            bag[item_id]["items_by_size"][size] = quantity
            new_qty = bag[item_id]["items_by_size"][size]
            messages.success(
                request,
                f"Updated size {size.upper()} {product.name} quantity to {new_qty}",
            )
        else:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(
                request,
                f"Removed size {size.upper()} {product.name} from your bag",
            )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f"Updated {product.name} quantity to {bag[item_id]}",
            )
        else:
            bag.pop(item_id)
            messages.success(
                request,
                f"Removed {product.name} from your bag",
            )

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """
    Remove a product or a specific size of a product from the shopping bag.

    Args:
        request (HttpRequest): The incoming HTTP request.
        item_id (str): ID of the product to remove.

    Returns:
        HttpResponse: HTTP status 200 if successful, 500 if error occurs.
    """
    product = get_object_or_404(Product, pk=item_id)

    try:
        size = request.POST.get("product_size")
        item_id = str(item_id)
        bag = request.session.get("bag", {})

        if size:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(
                request,
                f"Removed size {size.upper()} {product.name} from your bag",
            )
        else:
            bag.pop(item_id)
            messages.success(
                request,
                f"Removed {product.name} from your bag",
            )

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
