test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]
print('The original list is : ' + str(test_list))
res = list(zip(*temp))
print('The converted tuple list : ' + str(res))