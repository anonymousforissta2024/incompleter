#Source: https://stackoverflow.com/questions/48868516/type-error-with-django-post-method
from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # match list,
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.addTodo, name='add'),

    # match id goes to detail view
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]