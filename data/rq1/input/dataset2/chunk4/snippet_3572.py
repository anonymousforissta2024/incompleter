#Source: https://stackoverflow.com/questions/75031533/attributeerror-text-in-django
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chatbot_view, name="chatbot")
]