#Source: https://stackoverflow.com/questions/47733532/python-getting-typeerror-during-checking-whether-a-json-key-exist-or-not
json = json.dumps(results)
for profile in range (0, 10):
    if 'person' not in json['items'][profile]['pagemap']:
        org="null"
    else:
        org= results['items'][profile]['pagemap']['person'][0]['org']
        #results stores the json response.