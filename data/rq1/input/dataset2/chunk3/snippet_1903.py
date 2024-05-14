#Source: https://stackoverflow.com/questions/58188060/attributeerror-module-calc-views-has-no-attribute-home
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home')
]