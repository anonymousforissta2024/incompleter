#Source: https://stackoverflow.com/questions/47055600/how-to-convert-to-bytes-when-typeerror-cant-concat-bytes-to-str
import http.client

conn = http.client.HTTPSConnection("exampleurl.com")

payload = {
    'FilterId': "63G8Tg4LWfWjW84Qy0usld5i0f",
    'name': "Test",
    'description': "Test1",
    'deadline': "2017-12-31",
    'exclusionRuleName': "Exclude",
    'disable': "true",
    'type': "Type1"
    }

headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'x-csrf-token': "wWjeFkMcbopci1TK2cibZ2hczI",
    'cache-control': "no-cache",
    'postman-token': "23c09c76-3b030-eea1-e16ffd48e9"
    }


conn.request("POST", "/api/campaign/create", payload, headers)


res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))