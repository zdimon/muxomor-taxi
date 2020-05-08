from django.db import models

class City(models.Model):
    name = models.CharField(default='', max_length=250)
    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(default='', max_length=250)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name

class Point(models.Model):
    name = models.CharField(default='', max_length=250)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name
