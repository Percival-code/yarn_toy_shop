from django.contrib import admin

from yarn_toy_shop.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
