#Source: https://stackoverflow.com/questions/40000495/how-to-encode-bytes-in-json-json-dumps-throwing-a-typeerror
import base64
import json

data = {}
encoded = base64.b64encode(b'data to be encoded')
data['bytes'] = encoded

print(json.dumps(data))