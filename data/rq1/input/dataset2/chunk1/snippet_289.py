#Source: https://stackoverflow.com/questions/30401551/in-django-1-7-python3-using-floppyforms-1-3-keep-getting-error-typeerror-ob
import floppyforms as forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

class MyCustomForm(forms.ModelForm):
    user_name = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()

class Meta:
    model = MyCustomModel