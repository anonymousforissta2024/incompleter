my_list = ['p', 'q']
new_list = ['{}{}'.format(x, y) for y in range(1, n + 1) for x in my_list]
print(new_list)