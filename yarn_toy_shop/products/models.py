from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from yarn_toy_shop.photos.models import Photo

UserModel = get_user_model()


class Product(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
    name = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    product_photo = models.URLField(
        null=False,
        blank=False,
    )
    price = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)
