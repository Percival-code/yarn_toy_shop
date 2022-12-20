from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_view

from yarn_toy_shop.products.forms import ProductCreateForm
from yarn_toy_shop.products.models import Product


class ProductCreateView(generic_view.CreateView):
    template_name = 'products/add-product.html'
    model = Product
    form_class = ProductCreateForm


class ProductDetailsView(generic_view.DetailView):
    template_name = 'products/product-details.html'
    model = Product


class ProductEditView(generic_view.UpdateView):
    template_name = 'products/edit-product.html'
    model = Product
    fields = ('description', 'price')
    success_url = reverse_lazy('details product')


class ProductDeleteView(generic_view.DeleteView):
    template_name = 'products/edit-product.html'
    model = Product
    success_url = reverse_lazy('index')


class BuyProductView():
    pass
