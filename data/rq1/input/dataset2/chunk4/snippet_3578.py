#Source: https://stackoverflow.com/questions/43557978/getting-error-as-typeerror-at-add-follow-1-init-takes-1-positional-argu
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User

from django.db import models


# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='description default text')

    def __unicode__(self):
        return self.name


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    image = models.FileField()
    follow = models.ManyToManyField('self', blank=True)

    def __unicode__(self):
        return self.user