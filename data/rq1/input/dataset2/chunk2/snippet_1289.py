#Source: https://stackoverflow.com/questions/74878704/getting-error-typeerror-must-be-str-not-dict-when-substituting-variable-into
import json
from jsonpath_ng.ext import parse

with open('./movies.json') as movies_json:
    movies = json.load(movies_json)

recno = str(1)
query_main = f'parse("$.movies[{recno}]")'
jsonpath_expression = query_main
print('query main output is', (query_main))
print('query main type is', type(query_main))
print('jsonpath_expression type is', type(jsonpath_expression))
for match in jsonpath_expression.find(movies):
    print(match.value)