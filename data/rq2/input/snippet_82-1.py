from itertools import groupby
print('Original list:')
print(uno_list)
uno_list.sort()
print(uno_list)
print('\nSort the said unordered list:')
print(uno_list)
print('\nFrequency of the elements of the said unordered list:')
result = [len(list(group)) for key, group in groupby(uno_list)]
print(result)