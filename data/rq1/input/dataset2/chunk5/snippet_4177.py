#Source: https://stackoverflow.com/questions/61772088/ipython-name-error-name-x-is-not-defined
from __future__ import print_function
import sys
from IPython.utils._tokenize_py2 import String
sys.path.append('.')
import numpy, ctypes
Pylonlib = "/opt/pylon5/lib64/libpylonc.so"
from ctypes import cdll
libc = cdll.LoadLibrary(Pylonlib)
libc.PylonInitialize()
#### call any plyon function after you have initialized
libc.PylonTerminate()