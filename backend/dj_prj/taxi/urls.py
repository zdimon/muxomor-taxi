from django.urls import path, include

from taxi.views import RegionsListView, \
                       GoogleView, \
                       UserProfileSaveView, \
                       AddPointView, \
                       TripAddView, \
                       PassengerAddToTripView, \
                       DriverAddToTripView, \
                       SearchPointView, \
                       NotificationListView, \
                       Region2UserCreateView 



urlpatterns = [ 

        path('regions_list',RegionsListView.as_view()),
        path('google_auth',GoogleView.as_view()),
        path('profile_save',UserProfileSaveView.as_view()),
        path('point_add',AddPointView.as_view()),
        path('trip_add',TripAddView.as_view()),
        path('passenger_add_to_trip',PassengerAddToTripView.as_view()),
        path('driver_add_to_trip',DriverAddToTripView.as_view()),
        path('point_search',SearchPointView.as_view()),
        path('notification_list',NotificationListView.as_view()),
        path('region2user_add',Region2UserCreateView.as_view()),
 
]