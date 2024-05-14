#Source: https://stackoverflow.com/questions/43557978/getting-error-as-typeerror-at-add-follow-1-init-takes-1-positional-argu
"""stratinum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from imagec import views as imagec_views
from contact import views as contact_views
from django.conf.urls.static import static
from django.conf import settings
from django.core.urlresolvers import reverse


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', imagec_views.home, name='home'),
    url(r'^about/$', imagec_views.about, name='about'),
    url(r'^detail/$', imagec_views.detail, name='detail'),
    url(r'^profile/$', imagec_views.userProfile, name='profile'),
    url(r'^create_form/$', imagec_views.create_form, name='create_form'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^userProfile/$', contact_views.contact, name='userProfile'),
    url(r'^accounts/', include('allauth.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', imagec_views.ListaFollow, name="lista_follow"),
    url(r'^add_follow/(?P<id>\d{1,})/$', imagec_views.AddFollow, name='add_follow'),
    url(r'^remove_follow/(?P<id>\d{1,})/$', imagec_views.RemoveFollow, name='remove_follow')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)