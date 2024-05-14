#Source: https://stackoverflow.com/questions/59066080/attributeerror-module-django-contrib-auth-has-no-attribute-models-what-am
def calicutpara(request):
    return render(request, 'calicutpara.html')

class signup(CreateView):
    form_class = forms.userCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'