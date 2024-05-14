def split_list(lst, n):
    result = list((lst[i:i + n] for i in range(0, len(lst), n)))
    return result
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