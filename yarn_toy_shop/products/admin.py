from django.contrib import admin

from yarn_toy_shop.products.models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
