from collections import defaultdict
print('The original list is : ' + str(test_list))
freq_map = defaultdict(int)
for idx, val in test_list:
    freq_map[val] += 1
res = sorted(test_list, key=lambda ele: freq_map[ele[1]], reverse=True)
print('Sorted List of tuples : ' + str(res))