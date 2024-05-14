#Source: https://stackoverflow.com/questions/77687579/attributeerror-module-django-conf-global-settings-has-no-attribute-root-urlc
import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mojspecjalista.settings')

application = get_wsgi_application()