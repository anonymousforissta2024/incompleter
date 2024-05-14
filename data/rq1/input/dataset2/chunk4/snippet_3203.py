#Source: https://stackoverflow.com/questions/72217488/django-typeerror-field-id-expected-a-number-but-got-user
from django.db import models
from django.contrib.auth.models import User


class Notebook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name


class Notes(models.Model):
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title