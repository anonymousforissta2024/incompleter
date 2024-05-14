test_str = 'geeksforgeeks'
print('The original string is : ' + str(test_str))
temp = lambda sub: ''.join((chr for chr in sub if chr in set(K)))
res = K in temp(test_str)
print('Is substring in order : ' + str(res))