#Source: https://stackoverflow.com/questions/77687579/attributeerror-module-django-conf-global-settings-has-no-attribute-root-urlc
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('App.api.urls')),
    path('admin/', admin.site.urls),
]