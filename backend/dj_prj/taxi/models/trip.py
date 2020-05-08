from django.db import models

from taxi.models import UserProfile, Point

class Trip(models.Model):
    point_a = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='point_a')
    point_b = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='point_b')
    driver = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Trip2Passenger(models.Model):
    passenger = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='passenger')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)