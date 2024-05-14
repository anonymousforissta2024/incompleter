#Source: https://stackoverflow.com/questions/51439242/python-3-7-got-an-unexpected-typeerror-from-a-user-defined-function
xs = {'x': 1, 'y': 2, 'z': 0}
ys = {'a': 3, 'b': 4, 'c': 5}
def print_vector(x, y, z):
    print(f'<{x}, {y}, {z}>')

print_vector(**xs) # <1, 2, 0>
print_vector(**ys) # TypeError: print_vector() got an unexpected keyword argument 'a'