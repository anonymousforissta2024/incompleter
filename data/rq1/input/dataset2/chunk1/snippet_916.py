#Source: https://stackoverflow.com/questions/71743807/typeerror-reverse-takes-exactly-2-arguments-1-given
from django.urls import path

from . import views

urlpatterns = [
    path("api/v2/app/nextdialog", views.NextDialog.as_view(), name="app-next-dialog"),
]