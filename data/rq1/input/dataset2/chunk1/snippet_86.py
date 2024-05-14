#Source: https://stackoverflow.com/questions/6541767/python-urllib-error-attributeerror-bytes-object-has-no-attribute-read
import urllib.request
import json

response = urllib.request.urlopen('http://www.reddit.com/r/all/top/.json').read()
jsonResponse = json.load(response)

for child in jsonResponse['data']['children']:
    print (child['data']['title'])