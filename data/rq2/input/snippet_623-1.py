def access_elements(nums, list_index):
    result = [nums[i] for i in list_index]
    return result
nums = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
print('Original list:')
print(nums)
print('Index list:')
print(list_index)
print('\nItems with specified index of the said list:')
print(access_elements(nums, list_index))