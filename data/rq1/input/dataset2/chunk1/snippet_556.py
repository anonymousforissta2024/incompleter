#Source: https://stackoverflow.com/questions/52166054/typeerror-the-first-argument-must-be-callable-when-i-import-a-scheduler-in-my-v
from __future__ import print_function
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from datetime import datetime, timedelta
import requests
import schedule
import time


def republic(request):
    return HttpResponse("<h1>Success Hindustan</h1>")


def indiatv(request):
    return HttpResponse("<h1>Success Hindustan</h1>")

def ndtv(request):
    return HttpResponse("<h1>Success NDTV</h1>")


schedule.every().day.at("17:19").do(republic(requests))
schedule.every().day.at("17:19").do(indiatv(requests))
schedule.every().day.at("17:19").do(ndtv(requests))

while 1:
    schedule.run_pending()
    time.sleep(1)