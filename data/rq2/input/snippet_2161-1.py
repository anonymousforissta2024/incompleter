print('The original tuple is : ' + str(test_tup))
res = True
temp = set()
for ele in test_tup:
    if ele in temp:
        res = False
        break
    temp.add(ele)
print('Is tuple distinct ? : ' + str(res))