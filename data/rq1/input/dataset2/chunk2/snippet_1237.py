#Source: https://stackoverflow.com/questions/51426359/django-typeerror-nonetype-object-is-not-iterable-dont-understand-why-obje
from django.urls import path, re_path
# from qkchat import views
from .views import ThreadView, InboxView

app_name = 'qkchat'
urlpatterns = [
    path('', InboxView.as_view()),
    re_path(r'^(?P<username>[\w.@+-]+)/$', ThreadView.as_view()),
]