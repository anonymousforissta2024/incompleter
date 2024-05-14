#Source: https://stackoverflow.com/questions/49679171/nameerror-name-logs-is-not-defined-django-python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$/', views.index, name='index'),
]