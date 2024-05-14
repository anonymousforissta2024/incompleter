#Source: https://stackoverflow.com/questions/56956782/getting-typeerror-argument-should-be-integer-or-bytes-like-object-not-str
req = urllib2.Request(article.path, headers=settings.HDR)
html = urllib2.urlopen(req, timeout=settings.SOCKET_TIMEOUT_IN_SECONDS).read()
is_present = html.find(token_str) >= 0