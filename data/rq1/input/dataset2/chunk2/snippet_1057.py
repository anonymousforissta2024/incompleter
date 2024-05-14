#Source: https://stackoverflow.com/questions/50669942/typeerror-at-accounts-register-init-got-an-unexpected-keyword-argument
class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = '/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/login')
        else:
            return super(RegisterView, self).dispatch(*args, **kwargs)