from django_filters import FilterSet, NumberFilter, CharFilter
from taxi.models import Notifications

class NotificationFilter(FilterSet):
    user = NumberFilter()


    class Meta:
        model = Notifications
        fields = ['user']