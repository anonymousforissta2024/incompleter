from collections import defaultdict
test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
print('The original list is : ' + str(test_list))
freq_map = defaultdict(int)
for idx, val in test_list:
    freq_map[val] += 1
print('Sorted List of tuples : ' + str(res))