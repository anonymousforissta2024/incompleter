def test(nums):
    result = sorted([item for item in nums if item < 0])
    return result[0] + result[1]
print('Original list elements:')
print(nums)
print('Sum of two lowest negative numbers of the said array of integers: ', test(nums))
nums = [-4, 5, -2, 0, 3, -1, 4, 9]
print('\nOriginal list elements:')
print(nums)
print('Sum of two lowest negative numbers of the said array of integers: ', test(nums))