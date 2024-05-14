#Source: https://stackoverflow.com/questions/60274886/django-newbie-error-typeerror-view-must-be-a-callable-or-a-list-tuple-in-the
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,"myapp/templates/hello.html", {})