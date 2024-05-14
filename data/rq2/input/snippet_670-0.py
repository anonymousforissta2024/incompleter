def sum_column(nums, C):
    result = sum((row[C] for row in nums))
    return result
print('Original list of lists:')
print(nums)
column = 0
print('\nSum: 1st column of the said list of lists:')
print(sum_column(nums, column))
column = 1
print('\nSum: 2nd column of the said list of lists:')
print(sum_column(nums, column))
column = 3
print('\nSum: 4th column of the said list of lists:')
print(sum_column(nums, column))