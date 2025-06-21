from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
        "admin_actions",
    )
    ordering = ("sku",)
    list_filter = ("category",)
    search_fields = ("name", "sku", "description")

    def admin_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Edit</a> | '
            '<a class="button" href="{}">Delete</a>',
            f"/admin/products/product/{obj.id}/change/",
            f"/admin/products/product/{obj.id}/delete/",
        )

    admin_actions.short_description = "Actions"
    admin_actions.allow_tags = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
