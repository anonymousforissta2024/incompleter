#Source: https://stackoverflow.com/questions/38394598/typeerror-view-must-be-a-callable-or-a-list-tuple-in-the-case-of-include
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/$', "posts.views.post_home"), #posts is module and post_home 
]                                              # is a function in view. 