test_tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
print('The original tuple is : ' + str(test_tup))
res = [ele for ele in test_tup if not (tuple(ele) in temp or temp.add(tuple(ele)))]
print('The unique lists tuple is : ' + str(res))