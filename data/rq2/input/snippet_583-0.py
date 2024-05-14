import os
if os.path.isdir(path):
    print('\nIt is a directory')
elif os.path.isfile(path):
    print('\nIt is a normal file')
else:
    print('It is a special file (socket, FIFO, device file)')
print()