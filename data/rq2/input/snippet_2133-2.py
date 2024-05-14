test_str = 'geeksforgeeks is best'
print('The original string is : ' + str(test_str))
res = ''.join((idx if idx not in map_dict else map_dict[idx] for idx in test_str))
print('The converted string : ' + str(res))