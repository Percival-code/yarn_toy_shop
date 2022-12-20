from django.contrib import admin

from yarn_toy_shop.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
