#Source: https://stackoverflow.com/questions/50672941/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
from django.conf import settings
from django.db import models

# Create your models here.


class Tweet(models.Model):
    # user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)