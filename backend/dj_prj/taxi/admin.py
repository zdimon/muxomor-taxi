from django.contrib import admin
from taxi.models import City, Region, Point, SocialAuth, UserProfile, Trip2Passenger, Trip
from image_cropping import ImageCroppingMixin
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
    list_display = ['id', 'name', 'city', 'region']
    list_filter = ['city', 'region']

@admin.register(SocialAuth)
class SocialAuthAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'email', 'user', 'secret']


@admin.register(UserProfile)
class UserProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['id', 'publicname', 'phone', 'get_small_image_user', 'get_small_image_car']


class Trip2PassengerAdmin(admin.TabularInline):
    model = Trip2Passenger

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    inlines = [Trip2PassengerAdmin,]
    list_display = ['id', 'point_a', 'point_b', 'driver', 'price']