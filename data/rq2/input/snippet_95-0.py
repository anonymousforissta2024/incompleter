import json
print('Original String:')
print(j_str)
print('\nJSON data:')
print(json.dumps(j_str, sort_keys=True, indent=4))