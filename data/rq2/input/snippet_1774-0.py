from collections import OrderedDict
print('The original dictionary : ' + str(test_dict))
res = OrderedDict(reversed(list(test_dict.items())))
print('The reversed order dictionary : ' + str(res))