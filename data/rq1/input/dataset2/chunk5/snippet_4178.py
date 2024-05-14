#Source: https://stackoverflow.com/questions/57628352/recieving-an-attribute-error-when-trying-to-add-a-new-view
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(*args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")