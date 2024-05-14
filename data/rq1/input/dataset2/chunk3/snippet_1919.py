#Source: https://stackoverflow.com/questions/51715851/python-django-shell-attributeerror-article-object-has-no-attribute-title
from django.db import models

# Create your models here.
# A MODEL IS REPRESENTED BY CLASS

class Article(models.Model):
    title : models.CharField(max_length=100)
    slug  : models.SlugField()
    body  : models.TextField()
    date  : models.DateTimeField(auto_now_add=True)
    # ADD IN THUMNAILL LETTER

    def __str__(self):
        return self.title