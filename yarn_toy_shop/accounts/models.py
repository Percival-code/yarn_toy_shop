from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from yarn_toy_shop.core.validators import only_letter_validator


class AppUser(auth_models.AbstractUser):
    MAX_FIRST_NAME_LEN = 40
    MIN_FIRST_NAME_LEN = 1
    MAX_LAST_NAME_LEN = 40
    MIN_LAST_NAME_LEN = 1
    MIN_REQUIRED_AGE = 18

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

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        validators=(
            validators.MinValueValidator(MIN_REQUIRED_AGE),
        ),
        null=True,
        blank=True,
    )
