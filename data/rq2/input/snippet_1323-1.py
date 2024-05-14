def remove_column(nums, n):
    result = [i.pop(n) for i in nums]
    return result
list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
n = 0
print('Original Nested list:')
print(list1)
print('Extract 1st column:')
print(remove_column(list1, n))
n = 2
print('\nOriginal Nested list:')
print(list2)
print('Extract 3rd column:')
print(remove_column(list2, n))