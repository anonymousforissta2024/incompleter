#Source: https://stackoverflow.com/questions/36021291/django-python3-attributeerror-module-object-has-no-attribute-meta
from django import forms

class EmailForm(forms.Form):
    email = forms.TextInput()