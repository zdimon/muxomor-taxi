from django.db import models

from taxi.models import UserProfile, Point

class Trip(models.Model):
    point_a = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='point_a')
    point_b = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='point_b')
    driver = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s - %s' % (self.point_a, self.point_b)

class Trip2Passenger(models.Model):
    passenger = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='passenger')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)