#Source: https://stackoverflow.com/questions/49003357/type-error-in-get-wsgi-application-in-django-2-x-with-python3
import os
import sys

path = '/mypath'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Myapplication.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()