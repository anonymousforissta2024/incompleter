#Source: https://stackoverflow.com/questions/66959972/attributeerror-method-object-has-no-attribute-backend
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
import requests

client_id = "my_id"

def home_view(request: HttpRequest, *args, **kwargs):
    code = request.GET.get("code")
    user = exchange_code(code)
    authenticate(request, user=user)
    return render(request, "home.html", {})

def exchange_code(code: str):
    data = {
        "client_id": client_id,
        "client_secret": "my_secret",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8000/home/",
        "scope": "identify guilds"
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    credentials = response.json()
    
    access_token = credentials['access_token']
    response = requests.get('https://discord.com/api/v6/users/@me', headers={
        'Authorization': 'Bearer %s' % access_token
    })
    print(response)
    user = response.json()
    print(user)
    return user