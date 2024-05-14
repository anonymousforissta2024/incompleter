#Source: https://stackoverflow.com/questions/48868516/type-error-with-django-post-method
from django.db import models
from datetime import*
import time
from django.utils.timesince import timesince
from django.urls import*

class Task(models.Model):
    task_title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('todo:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.task_title