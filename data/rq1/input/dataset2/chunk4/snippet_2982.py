#Source: https://stackoverflow.com/questions/47953230/django-queryset-count-method-raise-typeerror-unorderable-types-nonetype
from django.db import models

class Device(models.Model):
    deviceClass     = models.CharField(max_length=10)

    class Meta:
        db_table = 'TST_G2S_DEVICE'