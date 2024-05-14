#Source: https://stackoverflow.com/questions/56159534/attributeerror-at-ask-module-django-db-models-has-no-attribute-student
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class post(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField(max_length=30)
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-post_date', )


class Lost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-post_date', )    


class Student(models.Model):
  first_name=models.CharField(max_length=15)
  last_name=models.CharField(max_length=15)
  age=models.IntegerField(default=15)
  date_birth=models.DateTimeField()
  def __str__(self):
    return self.first_name