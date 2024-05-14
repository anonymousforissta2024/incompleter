#Source: https://stackoverflow.com/questions/64486390/nameerror-when-trying-to-import-variables-from-another-python-file
# myfile1.py

x = 5
y = 2


# myfile2.py

from myfile1 import *

print(myfile1.x)
print(myfile1.y)