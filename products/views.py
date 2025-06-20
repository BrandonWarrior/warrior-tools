from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, WishlistItem
from .forms import ProductForm


def all_products(request):
    """Show all products with optional sorting, filtering, and search."""
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """Show details for a single product, including wishlist status."""
    product = get_object_or_404(Product, pk=product_id)
    in_wishlist = False

    if request.user.is_authenticated:
        in_wishlist = WishlistItem.objects.filter(
            user=request.user, product=product
        ).exists()

    context = {
        "product": product,
        "in_wishlist": in_wishlist,
    }
    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """Allow superusers to add a new product via a form."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/add_product.html", context)


@login_required
def edit_product(request, product_id):
    """Allow superusers to edit an existing product."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/edit_product.html", context)


@login_required
def delete_product(request, product_id):
    """Allow superusers to delete a product."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


@login_required
def toggle_wishlist(request, product_id):
    """Toggle the presence of a product in the user's wishlist."""
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user, product=product
    )

    if not created:
        wishlist_item.delete()
        messages.info(request, f"Removed {product.name} from your wishlist.")
    else:
        messages.success(request, f"Added {product.name} to your wishlist.")

    return redirect(request.META.get("HTTP_REFERER", "products"))
