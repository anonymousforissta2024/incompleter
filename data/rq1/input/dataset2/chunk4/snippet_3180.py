#Source: https://stackoverflow.com/questions/72095878/typeerror-create-superuser-missing-2-required-positional-arguments
import datetime
from django.core.mail import send_mail
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManger

GENDER_MALE = "m"
GENDER_FEMALE = "f"
OTHER = "o"

GENDER_CHOICES = (
    (GENDER_MALE, "Male"),
    (GENDER_FEMALE, "Female"),
    (OTHER, "Other"),
)


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    picture = models.ImageField(
        upload_to='images/users', null=True, verbose_name="")
    is_active = models.BooleanField(default=True)
    #is_staff = models.BooleanField(default=False)
    phone = PhoneNumberField()
    is_admin = models.BooleanField(default=False)
    #credits =models.PositiveIntegerField(default=100)
    linkedin_token = models.TextField(blank=True, default='')
    expiry_date = models.DateTimeField(null=True, blank=True)

    objects = UserManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name' , 'last_name']
    def get_full_name(self):
        full_name = '%S %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, prem, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perm(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
    ''''
    @property
    def is_staff(self):
        "Is the user a member of staff"
        return self.is_admin'''
    
    """@property
    def is_out_of_credits(self):
        "Is the user out of credits"
        return self.credits > 0
    @property
    def has_sufficient_credits(self,cost):
        return self.credits - cost >= 0
        """
    @property
    def linkedin_signed_in(self):
        return bool(self.linkedin_token) and self.expiry_date > timezone.now()