#Source: https://stackoverflow.com/questions/51466319/django2-attributeerror-in-urls-py
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')  