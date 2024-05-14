print('The original list is : ' + str(test_list))
delim = '$'
res = ''
for ele in test_list:
    res += str(ele) + '$'
res = res[:len(res) - 1]
print('The joined string : ' + str(res))