#Source: https://stackoverflow.com/questions/60274886/django-newbie-error-typeerror-view-must-be-a-callable-or-a-list-tuple-in-the
from django.conf.urls import include, url

urlpatterns = ['', url('hello/', 'views.hello', name='hello'),]