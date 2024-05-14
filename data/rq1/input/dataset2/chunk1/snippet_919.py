#Source: https://stackoverflow.com/questions/43055952/typeerror-modelbase-is-not-iterable
from django.conf.urls import url
from offense_api import views

urlpatterns = [
    url(r'^seasons/$', views.season_list),
    url(r'^seasons/(?P<pk>[0-9]+)/$', views.season_detail),
    url(r'^characters/$', views.character_list),
]