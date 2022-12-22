from django import forms

from yarn_toy_shop.core.form_mixins import DisabledFormMixin
from yarn_toy_shop.products.models import Product, Order


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'product_photo', 'price')


class ProductCreateForm(ProductBaseForm):
    pass


class ProductEditForm(DisabledFormMixin, ProductBaseForm):
    disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class ProductDeleteForm(ProductBaseForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class OrderBaseForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user', 'is_send')


class OrderMakeForm(OrderBaseForm):
    pass
