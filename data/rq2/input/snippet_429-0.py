def remove_none(nums):
    result = [x for x in nums if x is not None]
    return result
print('Original list:')
print(nums)
print('\nRemove None value from the said list:')
print(remove_none(nums))