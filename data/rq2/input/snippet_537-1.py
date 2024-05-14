def specified_element(nums, N):
    result = [i[N] for i in nums]
    return result
print('Original list of lists:')
print(nums)
N = 0
print('\nExtract every first element from the said given two dimensional list:')
print(specified_element(nums, N))
N = 2
print('\nExtract every third element from the said given two dimensional list:')
print(specified_element(nums, N))