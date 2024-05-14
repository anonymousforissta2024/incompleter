def specified_element(nums, N):
    result = [i[N] for i in nums]
    return result
nums = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
print('Original list of lists:')
print(nums)
print('\nExtract every first element from the said given two dimensional list:')
print(specified_element(nums, N))
N = 2
print('\nExtract every third element from the said given two dimensional list:')
print(specified_element(nums, N))