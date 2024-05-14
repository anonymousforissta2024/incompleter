#Source: https://stackoverflow.com/questions/56630585/how-can-i-solve-typeerror-at-post-new-in-django
# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from . models import Post

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'