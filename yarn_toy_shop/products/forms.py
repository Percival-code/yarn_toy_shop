from django import forms

from yarn_toy_shop.core.form_mixins import DisabledFormMixin
from yarn_toy_shop.products.models import Product


class ProductBaseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'product_photo')
        labels = {
            'name': 'Pet Name',
            'description': 'Description',
            'personal_photo': 'Link to Image',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            )
        }


class ProductCreateForm(ProductBaseForm):
    pass


class ProductEditForm(DisabledFormMixin, ProductBaseForm):
    disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class ProductDeleteForm(DisabledFormMixin, ProductBaseForm):
    disabled_fields = ('name', 'description', 'product_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
