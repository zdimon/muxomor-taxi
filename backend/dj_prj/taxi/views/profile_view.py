from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from taxi.serializers import ProfileSaveRequestSerializer
from taxi.models import UserProfile
from rest_framework.parsers import MultiPartParser

from rest_framework.serializers import ValidationError
from taxi.serializers import CommonSerializer, UserSerializer
import base64
from django.core.files.base import ContentFile

class UserProfileSaveView(APIView):
    """
    Saving user profile.

    _____________________

    """
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema( 
        request_body = ProfileSaveRequestSerializer, \
        responses={200: UserSerializer}
        )

    def post(self, request, format=None):

        try:
            user = UserProfile.objects.get(pk=request.data['user_id'])
        except:
            raise ValidationError('Error!!! the fucking user id is fucking wrong!!!')

        if "phone" in request.data:
            user.phone = request.data['phone']

        if "username" in request.data:
            user.username = request.data['username']

        if "publicname" in request.data:
            user.publicname = request.data['publicname']

        if "password" in request.data:
            user.set_password(request.data['password'])

        if "photo_user" in request.data:
            user.photo_user = (request.data['photo_user'])

        if "photo_car" in request.data:
            user.photo_user = (request.data['photo_car'])

        if "photo_user_base64" in request.data:
            format, imgstr = request.data.get('photo_user_base64').split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr))
            file_name = '%s_user.%s' % (user.id,ext) 
            user.photo_user.save(file_name, data, save=True)

        if "photo_car_base64" in request.data:
            format, imgstr = request.data.get('photo_car_base64').split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr))
            file_name = '%s_user.%s' % (user.id,ext) 
            user.photo_car.save(file_name, data, save=True)

        user.save()

        return Response(UserSerializer(user).data)