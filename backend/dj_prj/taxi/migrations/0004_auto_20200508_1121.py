# Generated by Django 3.0.6 on 2020-05-08 11:21

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0003_socialauth'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cropping_car',
            field=image_cropping.fields.ImageRatioField('image', '150x150', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping car'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cropping_user',
            field=image_cropping.fields.ImageRatioField('image', '150x150', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping user'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='photo_car',
            field=models.ImageField(blank=True, null=True, upload_to='photo_car'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='photo_user',
            field=models.ImageField(blank=True, null=True, upload_to='photo_user'),
        ),
    ]
