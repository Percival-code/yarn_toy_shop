from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models


class AppUser(auth_models.AbstractUser):
    MIN_REQUIRED_AGE = 18

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        validators=(
            validators.MinValueValidator(MIN_REQUIRED_AGE, message='You are under 18 years!'),
        ),
        null=True,
        blank=True,
    )
