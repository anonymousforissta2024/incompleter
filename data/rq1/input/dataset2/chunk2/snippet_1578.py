#Source: https://stackoverflow.com/questions/63318060/typeerror-formlistview-missing-1-required-positional-argument-request
from django.core.mail       import send_mail, BadHeaderError
from django.shortcuts       import render, redirect
from django.http            import HttpResponse, HttpResponseRedirect
from .models                import Form
from django.views.generic   import TemplateView

def FormListView(request):
    if request.method == 'GET':
        form = FormListView()
    else:
        form = FormListView(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            try:
                send_mail(name, surname, email, ['kirill_popov_000@mail.ru'])
            except BadHeaderError:
                return HttpResponse('Invalid')
            return redirect('success')
    return render(request, "index.html", {'form': form})

def Success(request):
    return HttpResponse('Success!')