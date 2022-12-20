from django.urls import path, include

from yarn_toy_shop.products.views import ProductDetailsView, ProductCreateView, ProductEditView, ProductDeleteView

urlpatterns = (
    path('<int:pk>/', include([
        path('', ProductDetailsView.as_view(), name='details product'),
        path('buy/', ProductDeleteView.as_view(), name='delete product'),
        path('add/', ProductCreateView.as_view(), name='add product'),
        path('edit/', ProductEditView.as_view(), name='edit product'),

    ])),
)
