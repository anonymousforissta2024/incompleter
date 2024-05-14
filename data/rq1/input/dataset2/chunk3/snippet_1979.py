#Source: https://stackoverflow.com/questions/62953908/attributeerror-tuple-object-has-no-attribute-get-django
from django.db import models

# Create your models here.
class ModelClas(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.IntegerField()
    passw = models.CharField(max_length=30)
    repass = models.CharField(max_length=30)