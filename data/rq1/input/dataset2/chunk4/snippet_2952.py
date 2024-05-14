#Source: https://stackoverflow.com/questions/73590895/attributeerror-wsgirequest-object-has-no-attribute-get-i-got-this-error-ear
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    objs = Project.objects.all()
    context = {"projects": objs}
    return render(request, 'projects/project.html', context)


def dynamic(request, text):
    obj = Project.objects.get(id=text)
    return render(request, 'projects/single-project.html', {'obj': obj})


def createproject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projectform.html', context)