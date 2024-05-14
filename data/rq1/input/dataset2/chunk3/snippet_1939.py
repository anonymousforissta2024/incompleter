#Source: https://stackoverflow.com/questions/61720078/django-typeerror-tuple-object-is-not-callable
from django.db import models

# Create your models here.

class Product(models.Model):
    ##contain all product information

    CONDITION_TYPE = (
        ("New" , "New")
        ("Used" , "Used")
    )

name = models.CharField(max_length=100)
description = models.TextField(max_length=500)
condition = models.CharField(max_length=100 , choices=CONDITION_TYPE)
price = models.DecimalField(max_digits=10, decimal_places=5)
created = models.DateTimeField()