from django.contrib import admin

from yarn_toy_shop.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
