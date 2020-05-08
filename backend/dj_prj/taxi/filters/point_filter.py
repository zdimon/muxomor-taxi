from django_filters import FilterSet, NumberFilter, CharFilter
from taxi.models import Point

class PointFilter(FilterSet):
    region = NumberFilter()
    searchkey = CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Point
        fields = ['region', 'searchkey']