test_str = 'void'
print('The original string is : ' + str(test_str))
res = ''
for ele in test_str:
    if ele in mir_dict:
        res += mir_dict[ele]
    else:
        res = 'Not Possible'
        break
print('The mirror string : ' + str(res))