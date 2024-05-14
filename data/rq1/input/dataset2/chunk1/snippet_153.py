#Source: https://stackoverflow.com/questions/16780359/nameerror-name-positivesmallintegerfield-is-not-defined
from django.db import models

class Song(models.Model):
    own = models.BooleanField(default=True)
    heard = models.DateTimeField(blank=True,null=True)
    release_date = models.DateField(blank=True,null=True)
    style = models.CharField(max_length=255,blank=True,null=True)
    artist = models.CharField(max_length=255,blank=True,null=True)
    featuring = models.CharField(max_length=255,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    listen = models.URLField(max_length=255,blank=True,null=True)
    highest_chart_pos = models.PositiveSmallIntegerField()
    note = models.TextField(blank=True,null=True)