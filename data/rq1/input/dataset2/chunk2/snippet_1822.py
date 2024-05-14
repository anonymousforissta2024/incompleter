#Source: https://stackoverflow.com/questions/56148087/how-to-fix-typeerror-argument-of-type-function-is-not-iterable-in-python
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
#from demoapp.form import ContactForm


# Create your views here.

def index(request):
    return render(request,'index.html',{'page':'home'})


def contact(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                send_mail(form.cleaned_data)
                messages.success(request,'Your message is successfully submitted')

        else:
            form = ContactForm()

    except:
        messages.error(request,'contact.html',{'page':'contact','form':form})

def clear(request):
    form = ContactForm()
    messages.error(request,'Fields Cleared')
    return render(request,'contact.html',{'page':'contact','form':form})