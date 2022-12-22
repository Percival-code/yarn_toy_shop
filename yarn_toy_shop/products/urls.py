from django.urls import path, include

from yarn_toy_shop.products.views import  create_product, ProductDetailsView, ProductEditView, delete_product, \
    make_order

urlpatterns = (
    path('add/', create_product, name='add product'),
    path('details/<int:pk>/', ProductDetailsView.as_view(), name='details product'),
    path('delete/<int:pk>/', delete_product, name='delete product'),
    path('edit/<int:pk>/', ProductEditView.as_view(), name='edit product'),
    path('buy/', make_order, name='make order'),

)
