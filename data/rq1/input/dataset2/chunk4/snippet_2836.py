#Source: https://stackoverflow.com/questions/66802437/attributeerror-int-object-has-no-attribute-append-getting-dict-out-of-two
from collections import defaultdict
final_dict = defaultdict(list)
list_keys= ['A', 'A', 'B', 'C']
list_values= [1,2,3,4]

for i in range(len(list_keys)):
    if list_keys[i] in final_dict:
        final_dict[list_keys[i]].append(list_values[i])
    else:
        final_dict[list_keys[i]] = list_values[i]