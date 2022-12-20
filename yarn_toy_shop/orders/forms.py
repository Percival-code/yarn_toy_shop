from django import forms

from django import forms

from yarn_toy_shop.orders.models import Order


class OrderBaseForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user',)
