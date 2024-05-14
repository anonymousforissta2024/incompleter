#Source: https://stackoverflow.com/questions/47027254/typeerror-write-argument-must-be-str-not-bytes-python-3-vs-python-2
import os
with open('random.bin','w') as f:
    f.write(os.urandom(10))