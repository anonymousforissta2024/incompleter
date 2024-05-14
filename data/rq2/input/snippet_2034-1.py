print('The original list is : ' + str(test_list))
K = 4
N = 3
res = [ele for ele in test_list if ele.count(K) == N]
print('Filtered tuples : ' + str(res))