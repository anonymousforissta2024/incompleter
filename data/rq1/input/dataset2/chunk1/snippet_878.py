#Source: https://stackoverflow.com/questions/47784216/django-rest-framework-attributeerror-function-object-has-no-attribute-model
from rest_framework.viewsets import ModelViewSet
from developers.models import Developers
from .serializers import DevSerializer


class DevViewSet(ModelViewSet):
    queryset = Developers.objects.all
    serializer_class = DevSerializer