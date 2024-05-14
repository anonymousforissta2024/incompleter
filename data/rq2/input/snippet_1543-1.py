test_dict = {'Gfg': 4, 'is': 2, 'best': 3, 'for': 'geeks'}
print('The original dictionary : ' + str(test_dict))
res = {key: val for key, val in test_dict.items() if type(val) != int or val > K}
print('Values greater than K : ' + str(res))