test_str = 'abababa'
print('The original string is : ' + str(test_str))
temp = [test_str[idx:j] for idx in range(len(test_str)) for j in range(idx + 1, len(test_str) + 1)]
for idx in temp:
    if idx not in res.keys():
        res[idx] = 1
    else:
        res[idx] += 1
print('Extracted frequency dictionary : ' + str(res))