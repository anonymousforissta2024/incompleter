#Source: https://stackoverflow.com/questions/67819164/typeerror-at-ap1-checkbooks-type-object-is-not-iterable-return-auth-for
from django.db import models

class BookNumber(models.Model):
    isbn_10=models.CharField(max_length=10,blank=True)
    isbn_30=models.CharField(max_length=12,blank=True)


# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=32)
    author=models.CharField(max_length=30)
    is_publise=models.BooleanField(default=False)
    publise_date=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    upload_time=models.DateField(auto_now_add=True,auto_now=False)#consider the current time.
    front_page=models.FileField(upload_to="content_folder/",default="")
    end_page_image=models.ImageField(upload_to="Image_folder/",blank=True)
    number=models.OneToOneField(BookNumber,null=True,blank=True,on_delete=models.CASCADE)#This line means only 1 isbn_10 & isbn_30 number will be assigned to one number in

    def __str__(self):
        return self.title