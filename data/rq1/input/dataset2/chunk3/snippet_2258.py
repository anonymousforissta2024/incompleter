#Source: https://stackoverflow.com/questions/63105190/how-to-resolve-typeerror-init-got-an-unexpected-keyword-argument-attrs
from django import forms
from phonenumber_field.formfields import PhoneNumberField



class UserAccount(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',     'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Surname'}))
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
    email = forms.CharField(widget=forms.EmailField(attrs={'class':'form-control', 'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    verify_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'verify password'}))