print('The original string is : ' + str(test_str))
sub_str = 'best'
res = test_str[:test_str.index(sub_str) + len(sub_str)]
print('The string after removal : ' + str(res))