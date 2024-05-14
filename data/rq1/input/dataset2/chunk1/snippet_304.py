#Source: https://stackoverflow.com/questions/30760728/python-3-urllib-produces-typeerror-post-data-should-be-bytes-or-an-iterable-of
import urllib.request, urllib.error, urllib.parse

url = "https://www.customdomain.com"
d = dict(parameter1="value1", parameter2="value2")

req = urllib.request.Request(url, data=urllib.parse.urlencode(d))
f = urllib.request.urlopen(req)
resp = f.read()