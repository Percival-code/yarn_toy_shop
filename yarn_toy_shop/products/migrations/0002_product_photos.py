# Generated by Django 4.1.4 on 2022-12-15 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photos',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.RESTRICT, to='photos.photo'),
            preserve_default=False,
        ),
    ]