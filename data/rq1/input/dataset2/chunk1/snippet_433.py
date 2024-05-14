#Source: https://stackoverflow.com/questions/63101250/i-am-getting-an-attribute-error-while-trying-to-build-a-user-registration-form-u
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),

]