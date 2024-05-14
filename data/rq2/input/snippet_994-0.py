def remove_column(nums, n):
    for i in nums:
        del i[n]
    return nums
n = 0
print('Original Nested list:')
print(list1)
print('After removing 1st column:')
print(remove_column(list1, n))
list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
n = 2
print('\nOriginal Nested list:')
print(list2)
print('After removing 3rd column:')
print(remove_column(list2, n))