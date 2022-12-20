from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from yarn_toy_shop.core.validators import telephone_number_length_validator, telephone_number_validator
from yarn_toy_shop.products.models import Product

UserModel = get_user_model()


class Order(models.Model):
    MAX_TELEPHONE_LENGTH = 12
    product = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    address = models.CharField(
        max_length=150,
        null=False,
        blank=False,
    )

    telephone_number = models.CharField(
        max_length=MAX_TELEPHONE_LENGTH,
        validators=(
            telephone_number_length_validator,
            telephone_number_validator,
        ),
        null=False,
        blank=False,
    )
