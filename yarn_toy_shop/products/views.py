from django.shortcuts import render
from django.views import generic as generic_view

from yarn_toy_shop.products.models import Product


class ProductDetailsView(generic_view.DetailView):
    template_name = 'products/product-details.html'
    model = Product