print('The original dictionary is : ' + str(test_dict))
temp = 'c'
res = [val[temp] for key, val in test_dict.items() if temp in val]
print('The extracted values : ' + str(res))