#Source: https://stackoverflow.com/questions/67819164/typeerror-at-ap1-checkbooks-type-object-is-not-iterable-return-auth-for
from django.urls import path,include
from rest_framework import routers
from .views import BookViewSet

router=routers.DefaultRouter()
router.register('books',BookViewSet)
urlpatterns=[
    path('check',include(router.urls)),
]