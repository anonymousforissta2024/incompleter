#Source: https://stackoverflow.com/questions/51426359/django-typeerror-nonetype-object-is-not-iterable-dont-understand-why-obje
from django import forms

class ComposeForm(forms.Form):
    message = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control",
                }
            )
        )