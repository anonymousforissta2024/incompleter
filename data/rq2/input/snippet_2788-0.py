print('Enter the row and column size:')
for out in range(ord(row_size), ord('A') - 1, -1):
    for i in range(ord(row_size), ord('A') - 1, -1):
        print(chr(out), end=' ')
    print('\r')