import copy
print('Original dictionary: ', nums_x)
nums_y = copy.copy(nums_x)
print('\nCopy of the said list:')
print(nums_y)
print('\nChange the value of an element of the original dictionary:')
nums_x['cc']['c'] = 10
print(nums_x)
print('\nSecond dictionary:')
print(nums_y)
nums = {'x': 1, 'y': 2, 'zz': {'z': 3}}
nums_copy = copy.copy(nums)
print('\nOriginal dictionary :')
print(nums)
print('\nCopy of the said list:')
print(nums_copy)
print('\nChange the value of an element of the original dictionary:')
nums['zz']['z'] = 10
print('\nFirst dictionary:')
print(nums)
print('\nSecond dictionary (copy):')
print(nums_copy)