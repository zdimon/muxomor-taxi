# Generated by Django 3.0.6 on 2020-05-08 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0012_region2user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region2user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.UserProfile'),
        ),
    ]
