#Source: https://stackoverflow.com/questions/67081201/django-throws-attributeerror-str-object-has-no-attribute-meta-when-i-regis
from django.contrib import admin
from .models import *

admin.site.register('Post')