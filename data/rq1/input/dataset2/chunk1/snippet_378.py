#Source: https://stackoverflow.com/questions/51466319/django2-attributeerror-in-urls-py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from core import views as coreviews

urlpatterns = ['',
    url(r'^$', coreviews.home), 
    path('admin/', admin.site.urls)
]