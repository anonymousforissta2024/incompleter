#Source: https://stackoverflow.com/questions/63756195/super-init-kwargs-typeerror-init-got-an-unexpected-keyword-argum
from django import forms
from .models import Student


class StudentRegistraion(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_num', 'email', 'password']
        widgets = {
            'name': forms.CharField(attrs={'class': 'form-control'}),
            'roll_num': forms.IntegerField(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),

        }