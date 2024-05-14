#Source: https://stackoverflow.com/questions/47784216/django-rest-framework-attributeerror-function-object-has-no-attribute-model
from rest_framework import serializers
from .models import Developers

class DevSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developers
        fields = ('name', 'surname', 'skills', 'education', 'employment_history')