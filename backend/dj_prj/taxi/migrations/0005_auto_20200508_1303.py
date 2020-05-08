# Generated by Django 3.0.6 on 2020-05-08 13:03

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_auto_20200508_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cropping_car',
            field=image_cropping.fields.ImageRatioField('photo_car', '150x150', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping car'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cropping_user',
            field=image_cropping.fields.ImageRatioField('photo_user', '150x150', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping user'),
        ),
    ]