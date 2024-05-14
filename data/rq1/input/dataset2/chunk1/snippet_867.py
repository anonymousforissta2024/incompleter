#Source: https://stackoverflow.com/questions/59066080/attributeerror-module-django-contrib-auth-has-no-attribute-models-what-am
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
app_name = 'login'

urlpatterns = [
    path('ktupage/', views.ktupage, name='ktupage'),
    path('mgcourses/', views.mgcourses, name='mgcourses'),
    path('calicutcourses/', views.calicutcourses, name='calicutcourses'),
    path('mgcourses/mgaas/', views.mgaas, name='mgaas'),
    path('mgcourses/mgpara/', views.mgpara, name='mgpara'),
    path('calicutcourses/calicutaas/', views.calicutaas, name='calicutaas'),
    path('calicutcourses/calicutpara/', views.calicutpara, name='calicutpara'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('signup/', views.signup.as_view(),name='signup'),
]