#Source: https://stackoverflow.com/questions/50669942/typeerror-at-accounts-register-init-got-an-unexpected-keyword-argument
class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['email', 'full_name']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        else:
            return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.get(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("A user with this email already exists.")
        else:
            return email

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False

        if commit:
            user.save()
        return user