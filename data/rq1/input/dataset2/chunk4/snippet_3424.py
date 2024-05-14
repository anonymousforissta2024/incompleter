#Source: https://stackoverflow.com/questions/73590895/attributeerror-wsgirequest-object-has-no-attribute-get-i-got-this-error-ear
from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'