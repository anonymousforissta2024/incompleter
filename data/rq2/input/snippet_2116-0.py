test_str = 'abababa'
print('The original string is : ' + str(test_str))
res = {}
for idx in temp:
    if idx not in res.keys():
        res[idx] = 1
    else:
        res[idx] += 1
print('Extracted frequency dictionary : ' + str(res))