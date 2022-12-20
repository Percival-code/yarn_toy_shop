from django.shortcuts import render
from django.urls import path

from yarn_toy_shop.common.views import index

urlpatterns = (
    path('', index, name='index'),
)