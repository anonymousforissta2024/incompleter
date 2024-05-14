from itertools import groupby
print('The original list : ' + str(test_list))
res = [list(val) for key, val in groupby(sorted(test_list))]
print('Matrix after grouping : ' + str(res))