#Source: https://stackoverflow.com/questions/69005427/typeerror-list-indices-must-be-integers-or-slices-not-str-even-after-following
import requests
import random
import string
import json

url = 'https://www.1secmail.com/api/v1/?action=getMessages&login=Demo&domain=1secmail.com'
r = requests.get(url)
raw = r.json()
print(raw["id"])