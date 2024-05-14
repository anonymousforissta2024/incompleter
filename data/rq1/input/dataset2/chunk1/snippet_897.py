#Source: https://stackoverflow.com/questions/5184483/python-typeerror-on-regex
url = 'http://google.com'
linkregex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')
m = urllib.request.urlopen(url)
msg = m.read()
links = linkregex.findall(msg)