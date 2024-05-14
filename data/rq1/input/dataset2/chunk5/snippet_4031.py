#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
from django.db import models

class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default='', null=True, blank=True, on_delete = models.CASCADE)