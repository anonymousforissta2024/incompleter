#Source: https://stackoverflow.com/questions/72559205/error-typeerror-at-admin-myapp-booking-19-change
#urls.py

from django.urls import path, include
from myapp.views import *
from rest_framework import routers





router = routers.DefaultRouter()
router.register('booking', BookViewSet, basename='MyModel')
urlpatterns = [

    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('flight/', FlightListCreateAPIView.as_view()),
    path('flight_info/<int:pk>/', FlightRetrtieveUpdateDestroyAPIView.as_view()),
    path('customer/', UserListCreateAPIView.as_view()),
    path('customer_info/<int:pk>/', UserRetrtieveUpdateDestroyAPIView.as_view()),
    path('passenger/', PassengerListCreateAPIView.as_view()),
    path('passenger_info/<int:pk>/', PassengerRetrtieveUpdateDestroyAPIView.as_view()),
    
    path('booking_info/<int:pk>/', BookingRetrtieveUpdateDestroyAPIView.as_view()),
    #path('booking/', BookingAPIView.as_view()),
    path('', include(router.urls)),
    

    
    
    
]