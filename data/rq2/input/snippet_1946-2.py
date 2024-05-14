test_str = 'zero four zero one'
print('The original string is : ' + test_str)
res = ''.join((help_dict[ele] for ele in test_str.split()))
print('The string after performing replace : ' + res)