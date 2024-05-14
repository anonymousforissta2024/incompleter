#Source: https://stackoverflow.com/questions/55058939/typeerror-create-got-multiple-values-for-keyword-argument-user
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from .models import Project, Module
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
from .serializers import ProjectSerializer, ModuleSerializer, TechnologySerializer, RequirementSerializer
from .models import *
from tags.models import Tag

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    """A viewset for viewing and manipulating user instances"""

    print("PROJECT VIEWSET")
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = 'slug'
    filter_backends = (DjangoFilterBackend, )

    @action(detail=True, methods=["GET"])
    def modules(self, request, id=None):
        project = self.get_object()
        modules = Module.objects.filter(project=project)
        serializer = ModuleSerializer(modules, many=True)

        return Response(serializer.data, status=200)

    @action(detail=True, methods=["GET"])
    def technologies(self, request, id=None):
        project = self.get_object()
        technologies = Technology.objects.filter(project=project)
        serializer = TechnologySerializer(technologies, many=True)

        return Response(serializer.data, status=200)

    @action(detail=True, methods=["GET"])
    def requirements(self, request, id=None):
        project = self.get_object()
        requirements = Requirement.objects.filter(project=project)
        serializer = RequirementSerializer(requirements, many=True)

        return Response(serializer.data, status=200)

    @action(detail=True, methods="POST")
    def project(self, request, id=None):
        print('POST')
        user = self.get_object()
        data = request.data
        print(data)
        data["user"] = user.id
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)