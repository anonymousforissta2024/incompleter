print('The original string is : ' + str(test_str))
map_dict = {'e': '1', 'b': '6', 'i': '4'}
res = ''.join((idx if idx not in map_dict else map_dict[idx] for idx in test_str))
print('The converted string : ' + str(res))