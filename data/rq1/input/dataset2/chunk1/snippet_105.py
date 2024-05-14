#Source: https://stackoverflow.com/questions/62807109/python-json-attributeerror-str-object-has-no-attribute-read
import json
fil='numbers.json'
num=[]
with open(fil,'r') as file :
    for obj in file :
        num.append(json.load(obj))
print(num)