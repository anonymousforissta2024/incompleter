#Source: https://stackoverflow.com/questions/59950609/typeerror-detail-missing-1-required-positional-argument-request
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import partial, Detailspartial, detail#

urlpatterns = [
        url(r'partial',partial,name="partial"),
        url(r'pardelete/(?P<pk>[0-9]+)/$', Detailspartial.as_view(), name="Partial details"),
        url(r'detail',detail,name="newfunction"),
]