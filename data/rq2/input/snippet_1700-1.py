test_str = 'geeksforgeeks'
print('The original string is : ' + str(test_str))
K = 'seek'
temp = lambda sub: ''.join((chr for chr in sub if chr in set(K)))
print('Is substring in order : ' + str(res))