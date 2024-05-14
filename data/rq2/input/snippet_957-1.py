from itertools import islice

def split_list(lst, n):
    lst = iter(lst)
    result = iter(lambda: tuple(islice(lst, n)), ())
    return list(result)
nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
print('Original list:')
print(nums)
print('\nSplit the said list into equal size', n)
print(split_list(nums, n))
n = 4
print('\nSplit the said list into equal size', n)
print(split_list(nums, n))
n = 5
print('\nSplit the said list into equal size', n)
print(split_list(nums, n))