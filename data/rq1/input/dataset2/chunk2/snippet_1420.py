#Source: https://stackoverflow.com/questions/43022570/urlretrieve-returning-typeerror
self.headers = { 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' }
self.request = urllib.request.Request(url, headers=self.headers)
urllib.request.urlretrieve(self.request, reporthook=report)