#Source: https://stackoverflow.com/questions/67212594/attributeerror-pathdistribution-object-has-no-attribute-name
from celery import Celery

app = Celery()
app.config_from_object('celeryconfig')