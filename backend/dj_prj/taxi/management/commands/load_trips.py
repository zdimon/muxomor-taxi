from django.core.management.base import BaseCommand, CommandError
import json
from dj_prj.settings import DATA_DIR, BASE_DIR
import os

from taxi.models import Trip, UserProfile, Point, Trip2Passenger
from django.core.files import File

class Command(BaseCommand):
   

    def handle(self, *args, **options):
        print('Loading trips....')
        Trip.objects.all().delete()
        admin = UserProfile.objects.get(username='admin')
        dima = UserProfile.objects.get(username='dima')
        nikita = UserProfile.objects.get(username='nikita')
        point_a = Point.objects.order_by('?').first()
        point_b = Point.objects.order_by('?').first()

        t = Trip()
        t.point_a = point_a
        t.point_b = point_b
        t.driver = admin
        t.price = 12
        t.save()

        t2u = Trip2Passenger()
        t2u.trip = t
        t2u.passenger = dima
        t2u.save()

        t2u = Trip2Passenger()
        t2u.passenger = nikita
        t2u.trip = t
        t2u.save()