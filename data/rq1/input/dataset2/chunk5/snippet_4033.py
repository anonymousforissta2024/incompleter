#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
#from django.contrib import admin
from django.urls import path, re_path
from lists import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path('^new/$', views.new_list, name="new_list"),
    re_path('^(\d+)/$', views.view_list, name="view_list"),
    re_path('^(\d+)/add_item$', views.add_item, name="add_item"),
]