#Source: https://stackoverflow.com/questions/57740763/getting-typeerror-byte-indices-must-be-integers-or-slices-not-str
from django.db import models

class Branches(models.Model):

    ifsc       = models.CharField(max_length=1009)
    bank_id    = models.IntegerField()
    branch     = models.CharField(max_length=1009)
    address    = models.CharField(max_length=1500)
    city       = models.CharField(max_length=1999)
    district   = models.CharField(max_length=1999)
    state      = models.CharField(max_length=1000)
    bank_name  = models.CharField(max_length=1000)


    def __str__(self):
        return self.branch

from urllib.request import urlopen, Request
from io import StringIO
import csv

for row in urlopen('https://raw.githubusercontent.com/snarayanank2/indian_banks/dc7ac64137ecf24bfc564f3d6151331215cf4783/bank_branches.csv'):
    Branches.objects.create(ifsc=row['ifsc'], bank_id=row['bank_id'], branch=row['branch'], address=row['address'], city=row['city'], district=row['district'], state=row['state'], bank_name=row['bank_name'])