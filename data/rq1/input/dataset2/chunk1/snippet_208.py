#Source: https://stackoverflow.com/questions/52675510/attributeerror-settings-object-has-no-attribute-auth-user-model-value-after
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StackOverflow.settings")

application = get_wsgi_application()