#Source: https://stackoverflow.com/questions/67819164/typeerror-at-ap1-checkbooks-type-object-is-not-iterable-return-auth-for
from rest_framework import viewsets
from .serializers import  BookSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    #Below line to give token authority
    authentication_classes = (TokenAuthentication)