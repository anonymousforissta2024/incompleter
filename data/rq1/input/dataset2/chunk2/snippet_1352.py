#Source: https://stackoverflow.com/questions/60274886/django-newbie-error-typeerror-view-must-be-a-callable-or-a-list-tuple-in-the
from django.contrib import admin

from django.urls import path,include
from django.conf.urls import url
admin.autodiscover()

urlpatterns = ['',
    path('admin/', admin.site.urls),
    url('myapp/', include('myapp.url'))
]