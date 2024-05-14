#Source: https://stackoverflow.com/questions/49309748/nameerror-name-django-filters-is-not-defined
from django.db import models
from django.contrib.postgres.search import SearchVectorField, SearchQuery
from django_filters import FilterSet



class Table1(models.Model, django_filters.FilterSet):
    field1 = models.IntegerField(db_column='field1', blank=True, null=True)  
    field2 = models.NullBooleanField(db_column='field2')  
    field3= models.IntegerField(db_column='field3', blank=True, null=True)  
    field4= models.TextField(db_column='field4', blank=True, null=False, primary_key=True)  

    #def __str__(self):
     #   return self.sid

    class Meta:
       managed = False
       db_table = 'Table1'
       unique_together = (('field1', 'field2', 'field3', 'field4'),)