spaces = size
for i in range(size // 2 + 2):
    for j in range(size):
        if j < i - 1:
            print(' ', end=' ')
        elif j > spaces:
            print(' ', end=' ')
        elif (i == 0 and j == 0) | (i == 0 and j == size - 1):
            print(' ', end=' ')
        else:
            print('*', end=' ')
    spaces -= 1
    print()