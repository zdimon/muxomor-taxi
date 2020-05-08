from django.urls import path, include

from taxi.views import RegionsListView


urlpatterns = [ 

        path('category_list',RegionsListView.as_view()),
 
]