#Source: https://stackoverflow.com/questions/49309748/nameerror-name-django-filters-is-not-defined
from django.shortcuts import render 
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.template import RequestContext
from django.views.generic import *

from .models import *
from .tables import *
from .forms  import *
from .filters import Table1Filter

def table1(request):
    filter = Table1Filter(request.GET, queryset=Table1.objects.all())
    return render(request, 'table1.html', {'filter': filter})