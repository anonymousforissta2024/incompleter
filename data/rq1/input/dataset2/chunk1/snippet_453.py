#Source: https://stackoverflow.com/questions/47784216/django-rest-framework-attributeerror-function-object-has-no-attribute-model
from django.db import models


class Education(models.Model):
    university =  models.CharField(max_length=50)
    year_of_graduation = models.DateField()


class Empl_history(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
    fr = models.DateField(verbose_name='from')
    to = models.DateField()


class Developers(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=30)
    skills = models.ForeignKey('Skills', on_delete=models.CASCADE)
    education = models.ManyToManyField(Education)
    employment_history = models.ManyToManyField(Empl_history)


class Skills(models.Model):
    SKILLS_CHOICES = (
    ('p', 'Python'),
    ('d',  'Django'),
    ('drf', 'Django Rest Framework'),
    )
    skills_choices = models.CharField(max_length=2, choices=SKILLS_CHOICES,)