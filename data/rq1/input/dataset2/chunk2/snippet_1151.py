#Source: https://stackoverflow.com/questions/67819164/typeerror-at-ap1-checkbooks-type-object-is-not-iterable-return-auth-for
from django.contrib import admin
from django.urls import path,include
#Below import for token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ap1/',include('ap1.urls')),
    path('auth/',obtain_auth_token),
]