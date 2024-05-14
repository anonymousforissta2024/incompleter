#Source: https://stackoverflow.com/questions/63313991/attributeerror-function-object-has-no-attribute-as-view-whats-wrong
from django.urls import path
from .views import FormListView

urlpatterns = [
    path('', FormListView.as_view(), name = 'home'),
    path('success/', Success.as_view(), name = 'success')
]