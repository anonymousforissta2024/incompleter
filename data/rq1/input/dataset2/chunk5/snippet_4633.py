#Source: https://stackoverflow.com/questions/73725398/i-am-getting-typeerror-view-must-be-a-callable-or-a-list-tuple-in-the-case-of
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('webarticles.urls')),
]