#Source: https://stackoverflow.com/questions/56159534/attributeerror-at-ask-module-django-db-models-has-no-attribute-student
from django import forms
from django.db import models

class UserRegistrar(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}  ))