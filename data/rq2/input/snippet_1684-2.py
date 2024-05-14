test_list = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]
print('The original list is : ' + str(test_list))
res = [idx for idx in test_list if (K, K) not in zip(idx, idx[1:])]
print('The records after removal : ' + str(res))