from django.core.management.base import BaseCommand, CommandError
import json
from taxi.models import City, Region, Point 
from dj_prj.settings import DATA_DIR
import os

class Command(BaseCommand):
   

    def handle(self, *args, **options):
        print('Loading regions....')
        City.objects.all().delete()
        Region.objects.all().delete()
        Point.objects.all().delete()
        
        dtf = open(os.path.join(DATA_DIR, 'regions.json'),'r')
        dt = json.loads(dtf.read())
        for city in dt:
            c = City()
            c.name = city['name']
            c.save()
            print('Saving.....%s' % c.name)
            for region in city['regions']:
                r = Region()
                r.city = c
                r.name = region['name']
                r.save()
                print('Saving.....%s' % r.name)
                for point in region['points']:
                    p = Point()
                    p.city = c
                    p.region = r
                    p.name = point['name']
                    p.save()
                    print('Saving.....%s' % p.name)

