from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from yarn_toy_shop.core.validators import telephone_number_length_validator, telephone_number_validator, \
    only_letter_validator
from yarn_toy_shop.products.models import Product

UserModel = get_user_model()


class Order(models.Model):
    MAX_FIRST_NAME_LEN = 40
    MIN_FIRST_NAME_LEN = 1
    MAX_LAST_NAME_LEN = 40
    MIN_LAST_NAME_LEN = 1
    MAX_TELEPHONE_LENGTH = 12

    product = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        validators=(
            validators.MinLengthValidator(MIN_FIRST_NAME_LEN),
            only_letter_validator,
        ),
        null=False,
        blank=False,

    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        validators=(
            validators.MinLengthValidator(MIN_LAST_NAME_LEN),
            only_letter_validator,
        ),
        null=False,
        blank=False,
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
