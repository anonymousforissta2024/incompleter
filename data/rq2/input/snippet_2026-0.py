print('The original list is : ' + str(test_list))
i, j = (3, 10)
res = True
for ele in test_list:
    if ele < i or ele >= j:
        res = False
        break
print('Does list contain all elements in range : ' + str(res))