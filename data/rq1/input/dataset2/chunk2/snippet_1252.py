#Source: https://stackoverflow.com/questions/56148087/how-to-fix-typeerror-argument-of-type-function-is-not-iterable-in-python
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from demoapp.views import index,about,contact,clear
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$' , index , name=index),
    url(r'^about/$' , about , name=about),
    url(r'^contact/$' , contact , name=contact),
    url(r'^clear/$' , clear , name=clear),


]