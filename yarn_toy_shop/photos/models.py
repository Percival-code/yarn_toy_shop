from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


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

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
