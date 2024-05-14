print('The original dictionary : ' + str(test_dict))
K = 3
res = {key: val for key, val in test_dict.items() if type(val) != int or val > K}
print('Values greater than K : ' + str(res))