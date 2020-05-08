from django.contrib.auth.models import User
from django.db import models

from image_cropping.fields import ImageRatioField, ImageCropField
from easy_thumbnails.files import get_thumbnailer

from dj_prj.settings import BACKEND_URL
from django.utils.safestring import mark_safe


class UserProfile(User):
    publicname = models.CharField(default='', max_length=250)
    phone = models.CharField(default='', max_length=250)
    photo_user = models.ImageField(upload_to='photo_user', null=True, blank=True)
    photo_car = models.ImageField(upload_to='photo_car', null=True, blank=True)
    cropping_user = ImageRatioField('photo_user', '150x150')
    cropping_car = ImageRatioField('photo_car', '150x150')

    @property
    def image_user_tag(self):
        return mark_safe('<img src="%s" />' % self.photo_user.url)

    @property
    def get_small_image_user(self):
        return mark_safe('<img src="%s" />' % self.get_small_image_user_url) 

    @property
    def get_small_image_user_url(self):
        try:
            return BACKEND_URL+get_thumbnailer(self.photo_user).get_thumbnail({
                'size': (100, 100),
                'box': self.cropping_user,
                'crop': 'smart',
            }).url 
        except:
            return BACKEND_URL+'noimage.png'   

    @property
    def image_car_tag(self):
        return mark_safe('<img src="%s" />' % self.photo_car.url)

    @property
    def get_small_image_car(self):
        return mark_safe('<img src="%s" />' % self.get_small_image_car_url) 

    @property
    def get_small_image_car_url(self):
        try:
            return BACKEND_URL+get_thumbnailer(self.photo_car).get_thumbnail({
                'size': (100, 100),
                'box': self.cropping_car,
                'crop': 'smart',
            }).url 
        except:
            return BACKEND_URL+'noimage.png'  