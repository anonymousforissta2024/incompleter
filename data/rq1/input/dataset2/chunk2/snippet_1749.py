#Source: https://stackoverflow.com/questions/51426359/django-typeerror-nonetype-object-is-not-iterable-dont-understand-why-obje
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from products import views
# from products.views import ProductListView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    # path('products/', ProductListView.as_view()),
    path('products/', include('products.urls')),
    path('auth/', include('social_django.urls', namespace='social')),  # social django url for oauth etc
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('ecom_home', views.ecom_home, name='ecom_home'),
    path('messages/', include('qkchat.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)