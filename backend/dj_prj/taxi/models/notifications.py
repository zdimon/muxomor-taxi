from django.db import models

from taxi.models import UserProfile, Point, Trip

class Notifications(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)