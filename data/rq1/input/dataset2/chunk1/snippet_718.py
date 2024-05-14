#Source: https://stackoverflow.com/questions/42956867/attributeerror-function-object-has-no-attribute-views
from django.conf.urls import url
from django.contrib import admin
import WarblerTest


urlpatterns = {
    url(r'^admin/', admin.site.urls),
    (r'^$', WarblerTest.blog.views.index),
    url(
        r'^blog/view/(?P<slug>[^\.]+).html',
        WarblerTest.blog.views.view_post,
        name='view_blog_post'),
    url(
        r'^blog/category/(?P<slug>[^\.]+).html',
        WarblerTest.blog.views.view_category,
        name='view_blog_category'),
}