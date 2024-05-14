#Source: https://stackoverflow.com/questions/50054662/django-admin-site-register-throws-typeerror-for-models-class
from django.contrib import admin
import inspect
from . import models 

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj):
        admin.site.register(obj)