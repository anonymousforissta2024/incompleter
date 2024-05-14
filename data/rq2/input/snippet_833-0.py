from itertools import groupby

def count_same_pair(nums):
    result = [sum((1 for _ in group)) for _, group in groupby(nums)]
    return result
print('Original lists:')
print(nums)
print('\nFrequency of the consecutive duplicate elements:')
print(count_same_pair(nums))