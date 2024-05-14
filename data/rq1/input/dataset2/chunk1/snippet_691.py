#Source: https://stackoverflow.com/questions/34572553/django-attributeerror-nonetype-object-has-no-attribute-split
from django.conf.urls import include, url

urlpatterns = [
    url(r'^page/(?P<slug>[-\w]+)/$', 'sitebuilder.views.page', name='page'),
    url(r'^page$', 'sitebuilder.views.page', name='homepage'),
]