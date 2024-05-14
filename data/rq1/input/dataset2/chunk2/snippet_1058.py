#Source: https://stackoverflow.com/questions/73704946/typeerror-type-object-is-not-iterable-drf
from django.db import models
from django.contrib.auth import get_user_model

import datetime

User = get_user_model()

class Actor(models.Model):
  name = models.CharField(max_length=255)
  first_name = models.CharField(max_length=255)

class Movie(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255, default='Description')
  date = models.DateTimeField(default=datetime.date.today)
  created_on = models.DateTimeField(auto_now_add = True)
  actors = models.ManyToManyField(Actor)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  def average_reviews(self):
    if hasattr(self, '_average_reviews'):
      return self._average_reviews
    return self.reviews.aggregate(models.Avg('mark'))
  
class Reviews(models.Model):
  mark = models.IntegerField(default=5)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)