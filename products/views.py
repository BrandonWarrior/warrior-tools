from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

import json  # To pass variant list into JS

# Variant types that use size selection
variant_options = [
    'hammer',
    'sds_drill',
    'drill_driver',
    'impact_driver',
    'jigsaw',
    'circular_saw',
    'orbital_sander',
    'tape_measure',
    'hand_saw',
]

# Tool types by category logic
HAND_TOOL_VARIANTS = [
    'hammer',
    'pliers',
    'tape_measure',
    'hand_saw',
    'pipe_cutter',
    'wood_chisel',
    'spirit_level',
]

POWER_TOOL_VARIANTS = [
    'sds_drill',
    'drill_driver',
    'impact_driver',
    'jigsaw',
    'circular_saw',
    'orbital_sander',
]

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category_filters = request.GET['category'].split(',')

            # Base category filter
            product_filter = Q(category__name__in=category_filters)

            expanded_categories = category_filters.copy()

            if 'hand_tools' in category_filters:
                product_filter |= Q(
                    category__name='new_arrivals',
                    variant_type__in=HAND_TOOL_VARIANTS
                )
                expanded_categories.append('new_arrivals')

            if 'power_tools' in category_filters:
                product_filter |= Q(
                    category__name='new_arrivals',
                    variant_type__in=POWER_TOOL_VARIANTS
                )
                expanded_categories.append('new_arrivals')

            products = products.filter(product_filter)
            categories = Category.objects.filter(name__in=expanded_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'variant_options': variant_options,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    context = {
        'form': form,
        'variant_options': json.dumps(variant_options),
    }

    return render(request, 'products/add_product.html', context)


def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    context = {
        'form': form,
        'product': product,
        'variant_options': json.dumps(variant_options),
    }

    return render(request, 'products/edit_product.html', context)
