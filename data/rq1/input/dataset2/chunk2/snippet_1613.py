#Source: https://stackoverflow.com/questions/61106188/i-am-getting-attributeerror-in-requestcontext-in-django
from django.conf.urls import url
from wfhApp import views

app_name = 'wfhApp'

urlpatterns = [
     url(r'^survey/$',views.survey, name='survey'),
]