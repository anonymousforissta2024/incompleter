import itertools
print('Original List', num)
num.sort()
new_num = list((num for num, _ in itertools.groupby(num)))
print('New List', new_num)