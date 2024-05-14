#Source: https://stackoverflow.com/questions/56347107/nameerror-name-values-is-not-defined
from django.db import models
...

class Car(models.Model, values):
    name = models.CharField(max_length=200)
    brand = values['brand']
    year = values['year']
    mpg = values['mpg']