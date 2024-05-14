#Source: https://stackoverflow.com/questions/73590895/attributeerror-wsgirequest-object-has-no-attribute-get-i-got-this-error-ear
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects),
    path('projects/<str:text>', views.dynamic, name='project'),
    path('create-project/', views.ProjectForm, name='create-project')
]