from django.contrib import admin
from taxi.models import City, Region, Point
# Register your models here.

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    list_filter = ['city']

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'region']
    list_filter = ['city', 'region']