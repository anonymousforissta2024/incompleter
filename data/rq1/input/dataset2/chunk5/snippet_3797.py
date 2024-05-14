#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
from django.urls import path, re_path, include
from lists import views as list_views
from lists import urls as list_urls

urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path('^$', list_views.home_page, name="home"),
    path('lists/', include(list_urls)),
    re_path('^lists/new/$', list_views.new_list, name="new_list"),
    re_path('^lists/(\d+)/$', list_views.view_list, name="view_list"),
    re_path('^lists/(\d+)/add_item$', list_views.add_item, name="add_item"),
]