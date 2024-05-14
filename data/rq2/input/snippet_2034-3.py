test_list = [(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)]
print('The original list is : ' + str(test_list))
N = 3
res = [ele for ele in test_list if ele.count(K) == N]
print('Filtered tuples : ' + str(res))