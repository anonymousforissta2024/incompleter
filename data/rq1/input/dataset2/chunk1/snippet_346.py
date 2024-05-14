#Source: https://stackoverflow.com/questions/5440485/typeerror-post-data-should-be-bytes-or-an-iterable-of-bytes-it-cannot-be-str
url = "http://example.com/index.php?app=core&module=global&section=login&do=process"
values = {"username" : USERNAME, 
          "password" : PASSWORD}
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data)
urllib.request.urlopen(req)