array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
print('Original arrays:')
print(array_nums)
odd_ctr = len(list(filter(lambda x: x % 2 != 0, array_nums)))
print('\nNumber of even numbers in the above array: ', even_ctr)
print('\nNumber of odd numbers in the above array: ', odd_ctr)