from django.core.management.base import BaseCommand, CommandError
import json
from dj_prj.settings import DATA_DIR
import os
from django.contrib.auth.models import User
from taxi.models import UserProfile

class Command(BaseCommand):
   

    def handle(self, *args, **options):
        print('Loading users....')
        User.objects.all().delete()
        
        dtf = open(os.path.join(DATA_DIR, 'users.json'),'r')
        dt = json.loads(dtf.read())
        for user in dt:
            u = UserProfile()
            u.username = user['username']
            u.set_password(user['password'])
            u.is_staff = True
            u.is_active = True
            u.is_superuser = True
            u.publicname = user['publicname']
            u.save()
            print('Saving.....%s' % u.username)
           