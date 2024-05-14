print('The original list is : ' + str(test_list))
K = 6
res = [idx for idx in test_list if (K, K) not in zip(idx, idx[1:])]
print('The records after removal : ' + str(res))