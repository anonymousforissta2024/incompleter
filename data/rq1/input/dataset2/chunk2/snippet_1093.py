#Source: https://stackoverflow.com/questions/67819164/typeerror-at-ap1-checkbooks-type-object-is-not-iterable-return-auth-for
from rest_framework import serializers
from . models import Book,BookNumber

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookNumber
        fields=['id','isbn_10','isbn_30']


class BookSerializer(serializers.ModelSerializer):
    number=BookNumberSerializer(many=False)
    class Meta:
        model=Book
        fields=['id','title','author','number']