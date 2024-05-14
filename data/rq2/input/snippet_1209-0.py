from itertools import combinations

def max_aggregate(l_data):
    max_pair = max(combinations(l_data, 2), key=lambda pair: pair[0] + pair[1])
    min_pair = min(combinations(l_data, 2), key=lambda pair: pair[0] + pair[1])
    return (max_pair, min_pair)
print('Original list:')
print(nums)
result = max_aggregate(nums)
print('\nMaximum aggregation pair of the said list of tuple pair:')
print(result[0])
print('\nMinimum aggregation pair of the said list of tuple pair:')
print(result[1])