from django.urls import path, include

from taxi.views import RegionsListView, GoogleView



urlpatterns = [ 

        path('category_list',RegionsListView.as_view()),
        path('google_auth',GoogleView.as_view()),
 
]