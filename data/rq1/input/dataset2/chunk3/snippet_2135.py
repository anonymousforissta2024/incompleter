#Source: https://stackoverflow.com/questions/58156230/filenotfounderror-winerror-3-the-system-cannot-find-the-path-specified
import os
from os import listdir

for i in range(9):
    for fld in folders:
        index = folders.index(fld)
        print('Load folders {} (Index: {})'.format(fld, index))
        path = os.path.join('Users', 'USER' , 'Desktop','ncfm' 'train', fld, '*.jpg')
        L.append(len(path))


    break