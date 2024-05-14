#Source: https://stackoverflow.com/questions/67137466/django-throwing-attribute-error-and-i-dont-know-why-it-is-happening
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from machine_website.models import contact_detail
from machine_website.models import product_data
from machine_website.forms import product_Form


# Create your views here.

def homepage(request):
    descp1 = product_data()
    descp1.disc = ' this is the discription'
    descp1.img = '2.jpg'

    descp2 = product_data()
    descp2.disc = ' this is the discription 2'
    descp2.img = '2.jpg'

    descp3 = product_data()
    descp3.disc = ' this is the discription 3'
    descp3.img = '5.jpg'

    descp = [descp1, descp2,descp3]
    return render(request,'homepage.html', {'descp': descp})

def contact(request):
    if request.method=="POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      desc = request.POST.get('desc')
      contact = contact_detail(name=name , email=email, desc=desc, date=datetime.today())
      contact.save()
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def index(request):
    return HttpResponse("this is index page")


def more(request):

    info = product_data.objects.all()

    return render(request ,'more.html' , {'info' : info})

IMAGE_FILE_TYPES = ['png' , 'PNG' , 'jpg' , 'JPG' , 'jpeg' , 'jfif']

def product_details(request):
    form = product_Form()
    if request.method == 'POST':
        form = product_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.img = request.FILES['img']
            file_type = user_pr.img.url.split('.')
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
               return render(request, 'error.html')
            user_pr.save()
            return render(request, 'details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'product_details.html', context)