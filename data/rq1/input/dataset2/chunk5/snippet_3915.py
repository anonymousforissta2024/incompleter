#Source: https://stackoverflow.com/questions/56159534/attributeerror-at-ask-module-django-db-models-has-no-attribute-student
from django.shortcuts import render, get_object_or_404
from .models import post
from .models import Lost
from .models import Student
from social import forms
from django.db import models



def home (request) :
    context = {
        'titel': 'homepage',
        'posts': post.objects.all()
    }
    return render (request, 'site.html', context) 


def post_detail(request, post_id):
    post= get_object_or_404(Lost, pk=post_id)
    context = {
        'title': post,
        'post': post,
    }

    return render(request, 'details.html', context)



def Register(request):

  form_data=forms.UserRegistrar(request.POST or None)
  msg=''
  if form_data.is_valid():
       student=models.Student()
       student.first_name=form_data.cleaned_data['first_name']
       student.last_name=form_data.cleaned_data['last_name']
       student.save()
       msg='data is saved'

  context={
        'formregister':form_data,
      'msg':msg
    }
  return render(request,'ask.html',context)