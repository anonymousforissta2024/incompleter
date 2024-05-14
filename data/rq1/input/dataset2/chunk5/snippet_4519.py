#Source: https://stackoverflow.com/questions/62442246/django-attribute-error-str-object-homepage
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.


class BlogListView(ListView):
    model = Posttemplate_name = 'home.html'