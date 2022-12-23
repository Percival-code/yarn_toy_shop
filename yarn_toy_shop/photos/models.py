from django.db import models

from yarn_toy_shop.products.models import Product


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='photos/',
        null=False,
        blank=False,
    )

    publication_date = models.DateField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    current_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
