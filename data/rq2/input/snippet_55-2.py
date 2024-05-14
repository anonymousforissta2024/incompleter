import itertools as it
mums1 = [1, 2, 3, 4]
mums2 = [5, 6, 7, 8]
mums3 = [9, 10, 11, 12]
print('Original lists:')
print(mums1)
print(mums2)
print(mums3)
print(mums4)
print('\nSum of the specified range:')
for i in it.product([tuple(mums1)], it.permutations(mums2), it.permutations(mums3), it.permutations(mums4)):
    print(i)