#Source: https://stackoverflow.com/questions/63318060/typeerror-formlistview-missing-1-required-positional-argument-request
from django.urls import path
from .views      import FormListView

urlpatterns = [
    path('',            FormListView(),     name = 'home'),
    path('success/',    Success(),          name = 'success')
]