#Source: https://stackoverflow.com/questions/59066080/attributeerror-module-django-contrib-auth-has-no-attribute-models-what-am
from django.db import models
from django.contrib import auth

class User(auth.models.User,auth.models.PermissionsMixin):

  def __str__(self):
      return "@{}".format(self.username)