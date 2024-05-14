#Source: https://stackoverflow.com/questions/62930892/if-model-meta-abstract-attributeerror-type-object-productobject-has-no-attr
from django.db import models as m
from django.conf import settings
import datetime

def mounth():
    now = datetime.datetime.now()
    return now + datetime.timedelta(days=20)

class Product(m.Model):
    product_name = m.CharField(max_length=200)
    product_calories = m.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.product_name


class Fridge(m.Model):
    OPTIONS = (
        ("1", "BASIC"),
        ("2", "PRO"),
        ("3", "KING"),
    )

    fridge_owner = m.ForeignKey(settings.AUTH_USER_MODEL, on_delete=m.CASCADE)
    fridge_mode = m.CharField(max_length=5, choices=OPTIONS)


class Recipe(m.Model):
    recipe_name = m.CharField(max_length=200)
    recipe_products = m.ManyToManyField(Product)
    recipe_description = m.TextField()

    def __str__(self):
        return self.recipe_name


class ProductObject(): # Не знаю как сделать правильно. Вдруг это можно реализовать по другому
    product_obj_fridge = m.ForeignKey(Fridge, on_delete=m.CASCADE)
    product_obj_product = m.ManyToManyField(Product)
    product_shelf_life = m.DateField(default=mounth())
    product_count = m.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('product_shelf_life', )