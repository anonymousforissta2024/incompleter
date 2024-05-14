from itertools import product
print('The original dictionary is : ' + str(test_dict))
res = dict(zip(test_dict['month'], test_dict['name']))
print('Flattened dictionary : ' + str(res))