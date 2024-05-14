#Source: https://stackoverflow.com/questions/56630585/how-can-i-solve-typeerror-at-post-new-in-django
# blog/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
]