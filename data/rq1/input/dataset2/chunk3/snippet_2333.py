#Source: https://stackoverflow.com/questions/59889563/typeerror-init-got-an-unexpected-keyword-argument-attrs
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from . models import Profile
from django.contrib.auth.models import User

ACCOUNT_TYPE = [
    ('SPO', 'SPO'),
    ('Call Agent', 'Call Agent'),
    ('Accountant', 'Accountant'),
]

class CreateUserForm(UserCreationForm):
    name            = forms.CharField(max_length=255, required=False)
    account_type    = forms.ChoiceField(choices = ACCOUNT_TYPE)

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'name': forms.CharField(attrs={'class': 'form-control','required':'required'}),
            'account_type': forms.ChoiceField(attrs={'class': 'form-control','required':'required'})
        }