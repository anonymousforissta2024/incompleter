from itertools import islice

def split_list(lst, n):
    lst = iter(lst)
    result = iter(lambda: tuple(islice(lst, n)), ())
    return list(result)
print('Original list:')
print(nums)
n = 3
print('\nSplit the said list into equal size', n)
print(split_list(nums, n))
n = 4
print('\nSplit the said list into equal size', n)
print(split_list(nums, n))
n = 5
print('\nSplit the said list into equal size', n)
print(split_list(nums, n))