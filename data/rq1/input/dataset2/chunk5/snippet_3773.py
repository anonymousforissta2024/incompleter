#Source: https://stackoverflow.com/questions/60559859/typeerror-list-expected-at-most-1-arguments-got-2
import os
import sys
listed=[]
for folderName,subfolders,filenames in os.walk('/'):
    for filename in filenames:
        if filename.endswith('.png'):
            listed.append(filename)
            for name in range(len(list(0,10))): 
                print(name)