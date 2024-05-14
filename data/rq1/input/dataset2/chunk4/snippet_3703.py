#Source: https://stackoverflow.com/questions/57584882/filenotfounderror-errno-2-no-such-file-or-directory-2mcrefe-jpg
import os
from PIL import Image

folder = '/Users/abc'
if not os.listdir(folder):
    print('Folder not found')
else:
    print('"{}" found'.format(folder))

for file in os.listdir(folder):
    print(file)
    data = Image.open(file,'r')
print('Done')