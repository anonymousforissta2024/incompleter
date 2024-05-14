#Source: https://stackoverflow.com/questions/72559205/error-typeerror-at-admin-myapp-booking-19-change
#models.py


import email
from pyexpat import model
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),)

class UserManager(BaseUserManager):
  def create_user(self, email, name,contact_number,gender,address,state,city,country,pincode,dob ,password=None, password2=None):
      
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          contact_number=contact_number,
          gender=gender,
          address=address,
          state=state,
          city=city,
          country=country,
          pincode=pincode,
          dob=dob,
          
      )

      user.set_password(password)
      
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name,contact_number,gender,address,state,city,country,pincode,dob , password=None):
     
      user = self.create_user(
          email,
          
          name=name,
          contact_number=contact_number,
          gender=gender,
          address=address,
          state=state,
          city=city,
          country=country,
          pincode=pincode,
          dob=dob,
          password=password,
          
      )
      user.is_admin = True
      user.save(using=self._db)
      return user



class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email',max_length=255,unique=True)
    name = models.CharField(max_length=200)
    contact_number= models.IntegerField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    address= models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    pincode= models.IntegerField()
    dob = models.DateField()


    # is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','contact_number','gender','address','state','city','country','pincode','dob']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# Create your models here.
class Airport(models.Model):
    Airport_name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __str__(self):
        return self.Airport_name

class Flight(models.Model):

    flight_number = models.CharField(max_length=100,unique=True)
    depart_date_time = models.DateTimeField(auto_now_add=True)
    arrival_date_time = models.DateTimeField(auto_now_add=True)
    origin = models.CharField(max_length=100, blank=True, default='')
    destination = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()
    airline_name = models.CharField(max_length=100, blank=True, default='')
    total_seats = models.IntegerField()
    available_seats =  models.IntegerField()
    
    
    airport=models.ForeignKey(Airport,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.flight_number)

   

class Passenger(models.Model):
    name = models.CharField(max_length=100,blank=True, default='')
    contact_number= models.IntegerField()
    email = models.EmailField(max_length=254)
    
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age= models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name  


class Booking(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    flights =models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger =models.ManyToManyField(Passenger)
    booking_number= models.CharField(max_length= 100,default=0, blank= True)
    booking_time = models.DateTimeField(auto_now_add=True)
    no_of_passengers= models.IntegerField(default=0, blank= True)

    def __str__(self):
        return self.booking_number