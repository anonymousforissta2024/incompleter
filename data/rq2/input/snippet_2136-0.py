test_dict = {'Gfg': {'a': 7, 'b': 9, 'c': 12}, 'is': {'a': 15, 'b': 19, 'c': 20}, 'best': {'a': 5, 'b': 10, 'c': 2}}
print('The original dictionary is : ' + str(test_dict))
res = [val[temp] for key, val in test_dict.items() if temp in val]
print('The extracted values : ' + str(res))