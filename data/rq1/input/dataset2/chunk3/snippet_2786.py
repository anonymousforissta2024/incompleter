#Source: https://stackoverflow.com/questions/68055130/attributeerror-at-akolaprofile-myregistration-object-has-no-attribute-get
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import FirstManager

class MyRegistration(AbstractBaseUser, PermissionsMixin):
    location_list=[
        ('Solapur', 'Solapur'),
        ('Latur', 'Latur'),
        ('Dhule', 'Dhule'),
        ('Akola', 'Akola'),
        ('Nashik', 'Nashik')
        ]
    username=models.CharField(max_length=10, unique=True)
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    location=models.CharField(max_length=10, choices=location_list, default='Latur')
    designation=models.CharField(max_length=70)
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    start_date=models.DateTimeField(default=timezone.now)
    last_login=models.DateTimeField(null=True)


    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email', 'first_name', 'last_name', 'location', 'designation']
    objects=FirstManager()
    def __str__(self):
        return self.username