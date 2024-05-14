#Source: https://stackoverflow.com/questions/59066080/attributeerror-module-django-contrib-auth-has-no-attribute-models-what-am
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class userCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'E-mail Address'