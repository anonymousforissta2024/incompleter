print('The original dictionary is : ' + str(test_dict))
max_val = 0
max_key = None
for sub in test_dict:
    if len(set(test_dict[sub])) > max_val:
        max_val = len(set(test_dict[sub]))
        max_key = sub
print('Key with maximum unique values : ' + str(max_key))