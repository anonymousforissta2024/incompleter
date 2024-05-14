from itertools import accumulate

def cumsum(lst):
    return list(accumulate(lst))
print('Original list elements:')
print(nums)
print('Cumulative sum of the elements of the said list:')
print(cumsum(nums))
nums = [-1, -2, -3, 4]
print('\nOriginal list elements:')
print(nums)
print('Cumulative sum of the elements of the said list:')
print(cumsum(nums))