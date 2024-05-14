#Source: https://stackoverflow.com/questions/50557668/django-typeerror-at-admin-login-has-module-perms-takes-2-positional-argume
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              unique=True, error_messages={'unique': 'Email is already occupied'})

    class Meta(AbstractUser.Meta):
        pass