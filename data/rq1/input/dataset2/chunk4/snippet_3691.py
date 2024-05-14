#Source: https://stackoverflow.com/questions/55058939/typeerror-create-got-multiple-values-for-keyword-argument-user
from rest_framework import serializers

from .models import Project, Module, Technology, Requirement
from tags.models import Tag
from accounts.models import User


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Project Tags"""

    class Meta:
        model = Tag
        fields = ('title',)


class RequirementSerializer(serializers.ModelSerializer):
    """Serializer for Project requirements"""

    class Meta:
        model = Requirement
        fields = ('name',)


class TechnologySerializer(serializers.ModelSerializer):
    """Serializer for Project technologies"""

    class Meta:
        model = Technology
        fields = ('name',)


class ModuleSerializer(serializers.ModelSerializer):
    """Serializer for Project Modules"""
    print("MODULES SERIALIZER")

    class Meta:
        model = Module
        fields = ('name',)


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project"""
    modules = ModuleSerializer(many=True)
    technologies = TechnologySerializer(many=True)
    requirements = RequirementSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'slug',
            'user',
            'title',
            'description',
            'price',
            'ratings',
            'modules',
            'technologies',
            'requirements',
            'tags'
            ]

    def create(self, validated_data):
        user = validated_data['user']
        modules = validated_data.pop('modules')
        technologies = validated_data.pop('technologies')
        requirements = validated_data.pop('requirements')
        tags = validated_data.pop('tags')
        user_key = User.objects.filter(id__iexact=user)
        project = Project.objects.create(**validated_data, user=user_key)
        for module in modules:
            Module.objects.create(**module, project=project)
        for technology in technologies:
            Technology.objects.create(**technology, project=project)
        for requirement in requirements:
            Requirement.objects.create(**requirement, project=project)
        for tag in tags:
            Tag.objects.create(**tag, project=project)

        return project