#Source: https://stackoverflow.com/questions/50037254/pathaccounts-includeaccounts-urls-nameerror-name-accounts-is-not-def
from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('accounts/', include(accounts.urls)),
]