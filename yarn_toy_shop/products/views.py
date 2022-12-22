from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as generic_view

from yarn_toy_shop.products.forms import ProductCreateForm, ProductDeleteForm, OrderMakeForm
from yarn_toy_shop.products.models import Product, Order


def create_product(request):
    if request.method == 'GET':
        form = ProductCreateForm()
    else:
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'products/add-product.html',
        context,
    )


class ProductDetailsView(generic_view.DetailView):
    template_name = 'products/product-details.html'
    model = Product


class ProductEditView(generic_view.UpdateView):
    template_name = 'products/edit-product.html'
    model = Product
    fields = ('name', 'price')
    success_url = reverse_lazy('index')


def delete_product(request, pk):
    product = Product.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = ProductDeleteForm(instance=product)
    else:
        form = ProductDeleteForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'products/delete-product.html',
        context,
    )


# TODO: deleting not ready check it


def make_order(request):
    if request.method == 'GET':
        form = OrderMakeForm()
    else:
        form = OrderMakeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'order/add-order.html',
        context,
    )


def handling_orders(request):
    orders = Order.objects.all().filter(is_send=False)
    context = {
        'orders': orders
    }
    return render(request, 'order/handling_orders.html', context)


def change_order_status(request, pk):
    current_order = Order.objects \
        .filter(pk=pk) \
        .get()

    current_order.is_send = True
    current_order.save()
    return redirect('handling orders')
