#Source: https://stackoverflow.com/questions/48276174/hickle-nameerror-name-file-is-not-defined
import os
import hickle as hkl
import numpy as np
array_obj = np.ones(32768, dtype='float32')
hkl.dump(array_obj, 'test.hkl', mode='w')