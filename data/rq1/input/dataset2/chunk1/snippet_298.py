#Source: https://stackoverflow.com/questions/31019854/typeerror-cant-use-a-string-pattern-on-a-bytes-like-object-in-re-findall
import urllib.request
import re

url = "http://www.google.com"
regex = r'<title>(,+?)</title>'
pattern  = re.compile(regex)

with urllib.request.urlopen(url) as response:
   html = response.read()

title = re.findall(pattern, html)
print(title)