#Source: https://stackoverflow.com/questions/34572553/django-attributeerror-nonetype-object-has-no-attribute-split
import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join

# Create your views here.

def get_page_or_404(name):
    """Returns page content as a Django template or raise 404 error"""
    try:
        file_path = safe_join(settings.STATIC_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404("Page Not Found")
    else:
        if not os.path.exists(file_path):
            raise Http404("Page Not Found")

    with open(file_path,"r", encoding='utf8') as f:
        the_page = Template(f.read())

    return the_page

def page(request, slug='index'):
    """ Render the requested page if found """
    file_name = '{0}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {'slug': slug, 'page': page} 
    return render(request, 'page.html', context)   # THE TRACEBACK POINTS AT THIS LINE, TOO