def first_index(l1):
    return sum((1 for i in l1 if i > 45 and i % 2 == 0))
print('Original list:')
print(nums)
n = 45
print('\nNumber of Items of the said list which are even and greater than', n)
print(first_index(nums))