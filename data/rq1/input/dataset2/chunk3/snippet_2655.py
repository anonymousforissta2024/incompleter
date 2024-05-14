#Source: https://stackoverflow.com/questions/63913377/typeerror-object-of-type-asia-kolkata-is-not-json-serializable
from django.db import models
from timezone_field import TimeZoneField
# Create your models here.
class Member(models.Model):
   tz = TimeZoneField(default='Asia/Kolkata')

   def __str__(self):
       return self.tz