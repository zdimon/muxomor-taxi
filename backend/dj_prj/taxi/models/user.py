from django.contrib.auth.models import User
from django.db import models

class UserProfile(User):
    publicname = models.CharField(default='', max_length=250)
    phone = models.CharField(default='', max_length=250)