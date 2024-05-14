#Source: https://stackoverflow.com/questions/57689928/why-am-i-getting-this-error-attributeerror-str-object-has-no-attribute-deco
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.register, name='register_user'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
]