print('The original list is : ' + str(test_list))
K = 'g'
res = []
for sub in test_list:
    temp = sub.split()
    for ele in temp:
        if ele[0].lower() == K.lower():
            res.append(ele)
print('The filtered elements : ' + str(res))