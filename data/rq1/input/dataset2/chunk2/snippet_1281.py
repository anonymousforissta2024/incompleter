#Source: https://stackoverflow.com/questions/55145601/the-json-object-must-be-str-not-list-typeerror
from django.shortcuts import render

# Create your views here.

import json
from .models import Movie

def detail(request):

    with open('movie_data.json', encoding='utf-8') as data_file:
        json_data = json.loads(data_file.read())
        print(type(json_data))

    json_dict = json.loads(json_data)
    for movie_data in json_dict:
        movie = Movie.create(**movie_data)
        # movie and genres created