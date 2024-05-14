def average_tuple(nums):
    result = tuple(map(lambda x: sum(x) / float(len(x)), zip(*nums)))
    return result
print('Original Tuple: ')
print(nums)
print('\nAverage value of the numbers of the said tuple of tuples:\n', average_tuple(nums))
nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
print('\nOriginal Tuple: ')
print(nums)
print('\nAverage value of the numbers of the said tuple of tuples:\n', average_tuple(nums))