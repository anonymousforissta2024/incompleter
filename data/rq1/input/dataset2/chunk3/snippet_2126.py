#Source: https://stackoverflow.com/questions/62406132/django-2-0-13-2-1-upgrade-causes-std-library-function-to-not-find-module-att
from uwsgi_tasks import set_uwsgi_callbacks, django_setup

set_uwsgi_callbacks()
django_setup()