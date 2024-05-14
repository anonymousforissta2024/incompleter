#Source: https://stackoverflow.com/questions/41323764/django-error-typeerror-init-got-an-unexpected-keyword-argument-attrs
from django.forms import ModelForm, TextInput, TextInput, EmailField
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('your_name', 'your_email', 'your_subject', 'your_comment')
        widgets = {
            'your_name' : TextInput(attrs={'placeholder': 'Name *', 'class': 'form-control'}),
            'your_email' : EmailField(attrs={'placeholder': 'Email *', 'class': 'form-control'}),
            'your_subject' : TextInput(attrs={'placeholder': 'Subject *', 'class': 'form-control'}),
            'your_comment' : Textarea(attrs={'placeholder': 'Comment *', 'class': 'form-control'}),
        }