from django.db import models
from taxi.models import UserProfile

class SocialAuth(models.Model):
    type = models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    secret =  models.CharField(max_length=250)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 