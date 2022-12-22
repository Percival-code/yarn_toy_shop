from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.utils.text import slugify

from yarn_toy_shop.core.validators import only_letter_validator, telephone_number_length_validator, \
    telephone_number_validator

UserModel = get_user_model()


class Product(models.Model):
    name = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    product_photo = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
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

    def __str__(self):
        return f'{self.name}'


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

    is_send = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )
