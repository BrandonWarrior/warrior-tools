"""
Admin configuration for the checkout app.

Registers the Order model with a customized admin interface that
displays order details and inline order line items.
"""

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin descriptor for OrderLineItem model.

    Displays line item details in a tabular inline form within the Order admin page.
    The lineitem_total field is read-only.
    """
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface for the Order model.

    Displays order information with inline editing of associated order line items.
    Several fields are marked read-only for data integrity.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "user_profile",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "county",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "delivery_cost",
        "grand_total",
    )

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
