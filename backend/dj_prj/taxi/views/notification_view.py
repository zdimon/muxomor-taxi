from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics


from taxi.models import Notifications
from taxi.serializers import NotificationSerializer
from taxi.filters import NotificationFilter


class NotificationListView(generics.ListAPIView):
    '''
    Search point.

    _______________________

    '''
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = NotificationFilter
