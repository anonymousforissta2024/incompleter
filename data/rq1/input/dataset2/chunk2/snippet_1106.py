#Source: https://stackoverflow.com/questions/43055952/typeerror-modelbase-is-not-iterable
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from offense_api.models import Episode, Season, Character
from offense_api.serializers import EpisodeSerializer, SeasonSerializer, CharacterSerializer


@csrf_exempt
def season_list(request):
    """
    List all seasons, or create a new one.
    :param request: 
    :return: 
    """
    if request.method == 'GET':
        seasons = Season.objects.all()
        serializer = SeasonSerializer(seasons, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SeasonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def season_detail(request, pk):
    """
    Retrieve, update, or delete a season.
    :param request: 
    :param pk: 
    :return: 
    """
    try:
        season = Season.objects.get(pk=pk)
    except Season.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SeasonSerializer(season)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SeasonSerializer(season, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        season.delete()
        return HttpResponse(status=204)


@csrf_exempt
def character_list(request):
    """
        List all characters, or create a new one.
        :param request: 
        :return: 
        """
    if request.method == 'GET':
        characters = Character.objects.all()
        serializer = CharacterSerializer(Character, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CharacterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)