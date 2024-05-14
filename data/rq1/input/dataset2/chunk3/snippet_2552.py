#Source: https://stackoverflow.com/questions/58188060/attributeerror-module-calc-views-has-no-attribute-home
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', include('calc.urls')),
    path('admin/', admin.site.urls),
]