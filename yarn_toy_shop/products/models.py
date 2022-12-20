from django.contrib.auth import get_user_model
from django.db import models

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

    photos = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
    )
