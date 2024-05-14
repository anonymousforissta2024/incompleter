#Source: https://stackoverflow.com/questions/65272979/importing-class-of-module-from-different-path-in-python-nameerror-name-enpy
import sys
sys.path.insert(1, '../enpy')

from enpy import *

# TESTING 

# 1. Creating Enpy Object
enpyObj = enpy.Enpy('./filetest/train.json')