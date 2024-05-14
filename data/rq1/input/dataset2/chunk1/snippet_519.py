#Source: https://stackoverflow.com/questions/42899389/typeerror-the-json-object-must-be-str-not-dict
data = json.loads(json_data)
data_set = (data['data'])
print(data_set)