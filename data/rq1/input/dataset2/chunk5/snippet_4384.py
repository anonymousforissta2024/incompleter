#Source: https://stackoverflow.com/questions/55257479/attributeerror-list-object-has-no-attribute-get-in-nested-dictionary
import json

with open('console_data.json', 'r') as console_data:
    parsed_data = console_data.read()
    nodes = json.loads(parsed_data)

last_node = nodes[-1]                   # extract last dictionary

print("\n\n\n")
for item in last_node:
    tags = last_node[item].get("Tags", {})
    try:
        print(tags)
    except AttributeError:
        pass