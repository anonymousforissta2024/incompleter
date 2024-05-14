#Source: https://stackoverflow.com/questions/58086723/python-urllib-request-urlopen-attributeerror-bytes-object-has-no-attribute
api_url = self.api_base+'/street2coordinates'
api_body = json.dumps(addresses)
#api_url=api_url.encode("utf-8")
#api_body=api_body.encode("utf-8")
print(type(api_url))
response_string = six.moves.urllib.request.urlopen(api_url, api_body).read()
response = json.loads(response_string)