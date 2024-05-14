#Source: https://stackoverflow.com/questions/47784216/django-rest-framework-attributeerror-function-object-has-no-attribute-model
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from developers import views

router = routers.DefaultRouter()
router.register(r'developers', views.DevViewSet)

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^api_demo', include(router.urls)),
]