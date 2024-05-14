#Source: https://stackoverflow.com/questions/49679171/nameerror-name-logs-is-not-defined-django-python
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logs/', include(logs.urls)),
]