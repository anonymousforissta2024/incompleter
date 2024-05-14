def remove_none(nums):
    result = filter(lambda v: v is not None, nums)
    return list(result)
print('Original list:')
print(nums)
print('\nRemove None value from the said list:')
print(remove_none(nums))