#Source: https://stackoverflow.com/questions/46050782/django-error-unsupported-operand-types-for-int-and-strtypeerror-at
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> Hi Cohen</h1>")