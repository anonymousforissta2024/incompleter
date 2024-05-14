test_tup = (1, 4, 5, 6, 1, 4)
print('The original tuple is : ' + str(test_tup))
res = True
for ele in test_tup:
    if ele in temp:
        res = False
        break
    temp.add(ele)
print('Is tuple distinct ? : ' + str(res))