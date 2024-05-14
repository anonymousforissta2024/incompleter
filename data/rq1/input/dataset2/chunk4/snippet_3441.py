#Source: https://stackoverflow.com/questions/73829248/unable-to-fetch-user-details-by-an-id-given-in-a-json-string-getting-a-type-er
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User, Team, Description
from .serializers import UserSerializer, TeamSerializer, DescriptionSerializer

# describe user
@api_view(["GET"])
def describe_user(request):
    user = User.objects.get(pk=request.data["id"])
    serializer = UserSerializer(user)
    return JsonResponse(serializer, safe=False)