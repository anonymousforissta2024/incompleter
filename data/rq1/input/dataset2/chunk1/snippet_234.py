#Source: https://stackoverflow.com/questions/38394598/typeerror-view-must-be-a-callable-or-a-list-tuple-in-the-case-of-include
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#function based views

def post_home(request):
    response = "<h1>Success</h1>"
    return HttpResponse(response)