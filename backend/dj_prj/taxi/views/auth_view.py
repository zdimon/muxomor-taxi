from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from taxi.serializers import GoogleAuthRequestSerializer, UserSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from taxi.models import UserProfile, SocialAuth

class GoogleView(APIView):
    '''
    Авторизация через гугл.

    _______________________

    '''
    
    permission_classes = (AllowAny,)
    @swagger_auto_schema( 
        request_body = GoogleAuthRequestSerializer \
        )
    def post(self, request, format=None):
        try:
            u = User.objects.get(username=request.data['email'])
            token = Token.objects.get(user=user)
            user = u.userprofile
        except Exception as e:
            print(str(e))
            user = UserProfile()
            user.username = request.data['email']
            user.publicname = '%s %s' % (request.data['name'],request.data['firstName'])
            user.is_active = True
            user.set_password = '123'
            user.save()
            token = Token.objects.create(user=user)
            s = SocialAuth()
            s.type = 'GOOGLE'
            s.email = request.data['email']
            s.user = user
            s.save()

        return Response({
            'token': token.key,
            'agent': request.META['HTTP_USER_AGENT'],
            'user': UserSerializer(user).data
        })