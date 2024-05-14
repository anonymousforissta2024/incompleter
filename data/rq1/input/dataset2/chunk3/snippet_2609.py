#Source: https://stackoverflow.com/questions/62953908/attributeerror-tuple-object-has-no-attribute-get-django
from django import forms
from .models import ModelClas

class FormClass(forms.ModelForm):
    passw = forms.CharField(widget=forms.PasswordInput())
    repass = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        super(FormClass, self).clean()
        inputpass = self.cleaned_data.get('passw')
        inputrepass = self.cleaned_data.get('repass')
        if inputpass != inputrepass:
           raise forms.ValidationError("Password not matched. please type again.")
        return inputpass, inputrepass

    class Meta:
        model = ModelClas
        fields = '__all__'