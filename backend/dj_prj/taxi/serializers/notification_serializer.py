from rest_framework import serializers
from taxi.models import Notifications

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notifications
        fields = ['id', 'trip', 'message', 'user']