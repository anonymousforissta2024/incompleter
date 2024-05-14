import os
Folderpath = 'C:/Users/Geetansh Sahni/Documents/R'
for path, dirs, files in os.walk(Folderpath):
    for f in files:
        fp = os.path.join(path, f)
        size += os.path.getsize(fp)
print('Folder size: ' + str(size))