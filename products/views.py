from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, WishlistItem
from .forms import ProductForm


def all_products(request):
    """ Show all products with sorting, filtering, and search """
    products = Product.objects.all()
    query = None
    categories = None
    current_sorting = ""

    if request.GET:
        # Sorting
        sort_param = request.GET.get("sort", "")
        if sort_param:
            if sort_param == "name_asc":
                products = products.annotate(lower_name=Lower("name"))
                products = products.order_by("lower_name")
            elif sort_param == "name_desc":
                products = products.annotate(lower_name=Lower("name"))
                products = products.order_by("-lower_name")
            elif sort_param == "price_asc":
                products = products.order_by("price")
            elif sort_param == "price_desc":
                products = products.order_by("-price")
            elif sort_param == "category_asc":
                products = products.order_by("category__friendly_name")
            elif sort_param == "category_desc":
                products = products.order_by("-category__friendly_name")
            elif sort_param == "rating_asc":
                products = products.order_by("rating")
            elif sort_param == "rating_desc":
                products = products.order_by("-rating")

            current_sorting = sort_param

        # Category filter
        if "category" in request.GET:
            raw_categories = request.GET.get("category", "")
            category_list = raw_categories.split(",")
            products = products.filter(category__name__in=category_list)
            categories = Category.objects.filter(name__in=category_list)

        # Search
        if "q" in request.GET:
            query = request.GET.get("q")
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ Display individual product details """
    product = get_object_or_404(Product, pk=product_id)
    in_wishlist = False

    if request.user.is_authenticated:
        in_wishlist = WishlistItem.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        "product": product,
        "in_wishlist": in_wishlist,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """ Add a new product (superuser only) """
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
                "Failed to add product. Please ensure the form is valid."
            )
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/add_product.html", context)


@login_required
def edit_product(request, product_id):
    """ Edit an existing product (superuser only) """
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
                "Failed to update product. Please ensure the form is valid."
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
    """ Delete a product (superuser only) """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


@login_required
def toggle_wishlist(request, product_id):
    """ Add or remove product from user's wishlist """
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item, created = WishlistItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        wishlist_item.delete()
        messages.info(
            request,
            f"Removed {product.name} from your wishlist."
        )
    else:
        messages.success(
            request,
            f"Added {product.name} to your wishlist."
        )

    referer = request.META.get("HTTP_REFERER", "products")
    return redirect(referer)
