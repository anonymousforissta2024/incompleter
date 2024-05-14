def access_elements(nums, list_index):
    result = [nums[i] for i in list_index]
    return result
print('Original list:')
print(nums)
list_index = [0, 3, 5, 7, 10]
print('Index list:')
print(list_index)
print('\nItems with specified index of the said list:')
print(access_elements(nums, list_index))