#Source: https://stackoverflow.com/questions/75031533/attributeerror-text-in-django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.url'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)