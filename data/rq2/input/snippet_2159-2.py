print('The original tuple is : ' + str(test_tup))
temp = set()
res = [ele for ele in test_tup if not (tuple(ele) in temp or temp.add(tuple(ele)))]
print('The unique lists tuple is : ' + str(res))