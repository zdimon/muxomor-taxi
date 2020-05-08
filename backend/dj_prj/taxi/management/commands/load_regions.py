from django.core.management.base import BaseCommand, CommandError
import json
from taxi.models import City, Region, Point 

class Command(BaseCommand):
   

    def handle(self, *args, **options):
        print('Loading regions....')
        