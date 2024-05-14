#Source: https://stackoverflow.com/questions/63343056/how-to-solve-nameerror-name-urllib2-is-not-defined-in-python-3-7
import urllib2.request

response = urllib2.urlopen("http://www.google.com")
html = response.read()
print(html)