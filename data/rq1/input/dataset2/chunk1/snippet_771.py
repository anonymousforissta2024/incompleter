#Source: https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete
from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class Article(models.Model):
    titre=models.CharField(max_length=100)
    auteur=models.CharField(max_length=42)
    contenu=models.TextField(null=True)
    date=models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name="Date de parution"
    )
    categorie = models.ForeignKey('Categorie')

    def __str__(self):
        return self.titre