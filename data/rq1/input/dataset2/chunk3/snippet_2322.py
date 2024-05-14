#Source: https://stackoverflow.com/questions/62930892/if-model-meta-abstract-attributeerror-type-object-productobject-has-no-attr
from django.contrib import admin
from .models import Product, Fridge, Recipe, ProductObject
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }

admin.site.register([Product, Fridge, ProductObject])
admin.site.register(Recipe, RecipeAdmin)