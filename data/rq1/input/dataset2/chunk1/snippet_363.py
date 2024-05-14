#Source: https://stackoverflow.com/questions/30760728/python-3-urllib-produces-typeerror-post-data-should-be-bytes-or-an-iterable-of
import urllib2
import urllib

url = "https://www.customdomain.com"
d = dict(parameter1="value1", parameter2="value2")

req = urllib2.Request(url, data=urllib.urlencode(d))
f = urllib2.urlopen(req)
resp = f.read()