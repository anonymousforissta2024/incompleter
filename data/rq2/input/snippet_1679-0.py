print('The original list is : ' + str(test_list))
res = []
for ele in test_list:
    if ele.strip():
        res.append(ele)
print('List after filtering non-empty strings : ' + str(res))