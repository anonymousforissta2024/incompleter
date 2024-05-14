#Source: https://stackoverflow.com/questions/61555925/typeerror-string-indices-must-be-integers-error-while-iterating-through-neste
api_request = requests.get('https://api.thevirustracker.com/free-api?countryTotals=ALL')

api = json.loads(api_request.content)

dict = api['countryitems'][0]

for key in dict:

    country = api['countryitems'][0][key]['title']
    print(country)