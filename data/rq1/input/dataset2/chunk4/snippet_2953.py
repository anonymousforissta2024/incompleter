#Source: https://stackoverflow.com/questions/71704716/typeerror-list-indices-must-be-integers-or-slices-not-str-error-appears-while
import requests
import xmltodict 

url = 'http://192.168.1.8:8060/query/apps'
text = requests.get(url).text
#content = """
#<?xml version="1.0" encoding="UTF-8"?>
#<apps>
#<app id="31012" type="menu" #version="2.0.53">Vudu Movie &amp; #TV Store</app>
#</apps>
#"""
text = text.split('\n')
text = text[1:]
text = ''.join(text)
data = xmltodict.parse(text)
data = dict(data)

for key1, value1 in data.items():
  for key2, value2 in value1.items():
    print(value2['@id'])
    print(value2['@type'])
    print(value2['#text'])