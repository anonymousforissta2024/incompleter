#Source: https://stackoverflow.com/questions/34619898/python3-typeerror-the-json-object-must-be-str-not-bytes
response = urllib.request.urlopen('http://api.icndb.com/jokes/random')
str_response = joke_json.readall().decode('utf-8')
obj = json.loads(str_response)