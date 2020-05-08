# Generated by Django 3.0.6 on 2020-05-08 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxi.UserProfile')),
            ],
        ),
    ]