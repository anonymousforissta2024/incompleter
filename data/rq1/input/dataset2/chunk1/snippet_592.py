#Source: https://stackoverflow.com/questions/34572553/django-attributeerror-nonetype-object-has-no-attribute-split
import os, shutil
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.test.client import Client

def get_pages():
    for name in os.listdir(settings.STATIC_PAGES_DIRECTORY):
        if name.endswith('.html'):
            yield name[:-5]


class Command(BaseCommand):
    help = 'Build static site output.'

    def handle(self, *args, **options):
        """Request pages and build output."""
        if os.path.exists(settings.SITE_OUTPUT_DIRECTORY):
            shutil.rmtree(settings.SITE_OUTPUT_DIRECTORY)
        os.mkdir(settings.SITE_OUTPUT_DIRECTORY) 
        os.makedirs(settings.STATIC_ROOT)   
        call_command('collectstatic', interactive=False, clear=True, verbosity=0)
        this_client_will = Client()

        for page in get_pages():
            the_page_url = reverse('page',kwargs={'slug': page})      # PROBLEM SEEMS TO GENERATE STARTING HERE
            response = this_client_will.get(the_page_url)
            if page == 'index.html':
                output_dir = settings.SITE_OUTPUT_DIRECTORY
            else:
                output_dir = os.path.join(settings.SITE_OUTPUT_DIRECTORY, page)
                os.makedirs(output_dir)
            with open(os.path.join(output_dir, 'index.html'), 'wb', encoding='utf8') as f:
                f.write(response.content)