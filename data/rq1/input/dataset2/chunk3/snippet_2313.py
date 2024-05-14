#Source: https://stackoverflow.com/questions/58030538/typeerror-str-object-is-not-callable-on-request-to-api
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers


class ListBrand(APIView):
    def get(self, request, format=None):
        brands = models.Brand.objects.all()
        serializer = serializers.BrandSerializer(brands, many=True)
        data = serializer.data
        return Response(data)