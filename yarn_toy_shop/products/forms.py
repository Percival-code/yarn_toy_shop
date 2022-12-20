from django import forms

from yarn_toy_shop.products.models import Product


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user', 'photos')
