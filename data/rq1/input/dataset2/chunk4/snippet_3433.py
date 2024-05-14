#Source: https://stackoverflow.com/questions/65725015/typeerror-module-object-is-not-callable-django-3-render-function
from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import RequestContext, loader
# from django.template import Context

def index(request):
    """Placeholder index view"""
    print('XXXX')
    return render(request, 'hello_world/index.html')
    #return HttpResponse('Hello, World!')

def test(request):
    context = {'foo': 'bar'}
    return render(request, 'hello_world/index.html', context) 