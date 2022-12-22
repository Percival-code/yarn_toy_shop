from django.contrib.auth import get_user_model
from django.shortcuts import render

from django.views.generic import TemplateView

from yarn_toy_shop.accounts.forms import UserCreateForm
from yarn_toy_shop.products.models import Product

UserModel = get_user_model()


def index(request):
    # if request.user.is_authenticated:
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)

# else:
#
#     if request.method == 'GET':
#         form = UserCreateForm(instance=UserModel)
#     else:
#         form = UserCreateForm(request.POST, instance=UserModel)
#         if form.is_valid():
#             form.save()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'home/register.html', context)
