from django.urls import path

from yarn_toy_shop.products.views import ProductDetailsView

urlpatterns = (
    path('details/', ProductDetailsView.as_view(), name='details product'),
)