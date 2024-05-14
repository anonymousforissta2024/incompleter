#Source: https://stackoverflow.com/questions/73825029/error-when-defining-a-dictionary-path-as-a-variable-typeerror-string-indices-m
def updateJson(fileName, pathToValue, updatedValue):
    # Opening JSON file
    f = open(fileName)
    # returns JSON object as a dictionary
    data = json.load(f)
    # Changes the ID value in JSON
    data[pathToValue] = updatedValue

    f.close()
    with open("template3.json", "w") as outfile:
        json.dump(data, outfile)
   
x = ['Something 1'][0]['ID']

updateJson("Temp\\random.json", x, 9) 