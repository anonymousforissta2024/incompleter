#Source: https://stackoverflow.com/questions/74878704/getting-error-typeerror-must-be-str-not-dict-when-substituting-variable-into
import json
from jsonpath_ng.ext import parse

with open('./movies.json') as movies_json:
    movies = json.load(movies_json)

jsonpath_expression = parse("$.movies[1]")
print('jsonpath_expression type is', type(jsonpath_expression))
for match in jsonpath_expression.find(movies):
    print(match.value)