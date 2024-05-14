from collections import Counter
print('The original list is : ' + str(test_list))
res = [(*key, val) for key, val in Counter(test_list).items()]
print('Frequency Tuple list : ' + str(res))