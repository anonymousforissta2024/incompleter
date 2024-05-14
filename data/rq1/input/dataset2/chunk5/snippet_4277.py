#Source: https://stackoverflow.com/questions/55383614/i-am-getting-typeerror-when-trying-to-print-a-value-loaded-from-a-json-file
import json
with open('input.json', 'r') as input:
    obj = json.load(input)
    print('Hello, ' + obj['hobbies'])