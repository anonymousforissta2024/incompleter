#Source: https://stackoverflow.com/questions/67015173/django-rest-api-attributeerror-the-serializer-field-might-be-named-incorrectly
from rest_framework import serializers

class ConstituentNameLists(serializers.Serializer):
    '''
    Returns Index Constituents
    '''
    strings = serializers.ListField(
        child = serializers.CharField(max_length=100)
    )