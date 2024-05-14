print('Enter the row and column size:')
for out in range(ord('A'), ord(row_size) + 1):
    for i in range(ord('A'), ord(row_size) + 1):
        print(chr(i), end=' ')
    print('\r')