#Source: https://stackoverflow.com/questions/62757155/typeerror-field-id-expected-a-number-but-got-user
from django.contrib import admin
from .models import BlogPost
# Register your models here.
admin.site.register(BlogPost)