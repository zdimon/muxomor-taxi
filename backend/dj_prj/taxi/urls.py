from django.urls import path, include

from taxi.views import RegionsListView, GoogleView, UserProfileSaveView



urlpatterns = [ 

        path('category_list',RegionsListView.as_view()),
        path('google_auth',GoogleView.as_view()),
        path('profile_save',UserProfileSaveView.as_view()),
 
]