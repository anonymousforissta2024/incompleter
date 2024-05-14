#Source: https://stackoverflow.com/questions/62362926/getting-typeerror-init-missing-1-required-positional-a-rgument-on-delet
from django.db import models
# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.top_name
class Webpage(models.Model):
    topic= models.ForeignKey(Topic)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique= True)

    def __str__(self):
        return self.name
class AccessRecord(models.Model):
        name = models.ForeignKey(Webpage)
        date = models.DateField()

        def __str__(self):
            return str(self.date)