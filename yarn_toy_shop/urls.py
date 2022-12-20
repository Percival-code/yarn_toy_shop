from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('yarn_toy_shop.common.urls')),
    path('accounts/', include('yarn_toy_shop.accounts.urls')),
    path('orders/', include('yarn_toy_shop.orders.urls')),
    path('photos/', include('yarn_toy_shop.photos.urls')),
    path('products/', include('yarn_toy_shop.products.urls')),
]
