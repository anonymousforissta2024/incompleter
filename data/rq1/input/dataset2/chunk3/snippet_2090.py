#Source: https://stackoverflow.com/questions/58188060/attributeerror-module-calc-views-has-no-attribute-home
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World !")