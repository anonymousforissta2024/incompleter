#Source: https://stackoverflow.com/questions/51661377/appending-json-file-typeerror-list-indices-must-be-integers-or-slices-not-st
filepath = os.path.join('filename.json')   
with open(filepath) as jsonfile:
    json_data = json.load(jsonfile)

    for i in range(len(json_data)):
        itemId = json_data[i]['itemId']
        print(itemId)