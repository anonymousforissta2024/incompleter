def first_index(l1):
    return sum((1 for i in l1 if i > 45 and i % 2 == 0))
nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
print('Original list:')
print(nums)
print('\nNumber of Items of the said list which are even and greater than', n)
print(first_index(nums))