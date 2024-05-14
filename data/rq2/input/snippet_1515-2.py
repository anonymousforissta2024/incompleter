test_list = [4, 7, 8, 3, 2, 1, 9]
print('The original list is : ' + str(test_list))
delim = '$'
for ele in test_list:
    res += str(ele) + '$'
res = res[:len(res) - 1]
print('The joined string : ' + str(res))