bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('Base numbers abd index: ')
print(bases_num)
print(index)
result = list(map(pow, bases_num, index))
print('\nPower of said number in bases raised to the corresponding number in the index:')
print(result)