#Source: https://stackoverflow.com/questions/63840651/how-to-handle-this-typeerror-in-string-requires-string-as-left-operand-not
import os
from os import path
import shutil

src = "D:/folder2"
dst = "D:/folder1"

files = [i for i in os.listdir(src) if ('7809.txt','988876.txt') in i and path.isfile(path.join(src, i))]
for f in files:
    shutil.copy(path.join(src, f), dst)