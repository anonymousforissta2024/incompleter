#Source: https://stackoverflow.com/questions/77422709/django-attributeerror-type-object-has-no-attribute-meta
import django_filters
from .models import AppUserManager

class AppUserManagerFilter(django_filters.FilterSet):
    class Meta:
        model = AppUserManager
        fields = {
            'email': ['exact', 'icontains'],
            'is_superuser': ['exact'],
            'is_staff': ['exact'],
            'is_active': ['exact'],
        }