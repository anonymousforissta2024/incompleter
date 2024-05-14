#Source: https://stackoverflow.com/questions/61106188/i-am-getting-attributeerror-in-requestcontext-in-django
from django.shortcuts import render
from django.template import RequestContext

def survey(request):
    return render(RequestContext(request),'wfhApp/survey.html')