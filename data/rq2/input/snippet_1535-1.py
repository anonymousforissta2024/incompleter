test_str = 'geeksforgeeks'
print('The original string is : ' + str(test_str))
res = ''
for idx in range(len(test_str)):
    if idx >= hlf_idx:
        res += test_str[idx].upper()
    else:
        res += test_str[idx]
print('The resultant string : ' + str(res))