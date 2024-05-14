from functools import reduce

def mutiple_list(nums):
    result = reduce(lambda x, y: x * y, nums)
    return result
print('Original list: ')
print(nums)
print('Mmultiply all the numbers of the said list:', mutiple_list(nums))
nums = [2, 4, 8, 8, 3, 2, 9]
print('\nOriginal list: ')
print(nums)
print('Mmultiply all the numbers of the said list:', mutiple_list(nums))