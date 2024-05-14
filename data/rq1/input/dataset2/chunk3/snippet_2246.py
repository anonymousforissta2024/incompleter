#Source: https://stackoverflow.com/questions/53260022/django-with-postgres-backend-attribute-error
from django.db import models as m
import django.contrib.postgres as pg

class node(m.Model):
    inputfile = m.CharField(max_length = 255)
    source_id = m.IntegerField()
    source_sim = m.CharField(max_length = 255)
    coordinates = pg.fields.ArrayField(m.FloatField(), size = 3)