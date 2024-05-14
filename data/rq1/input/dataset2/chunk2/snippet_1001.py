#Source: https://stackoverflow.com/questions/62632134/python-string-to-array-typeerror-iteration-over-a-0-d-array
import numpy as np
tags = "[{'thirdParty': 'Funds Transfer'}, {'category': 'External Transfers'}, {'creditDebit': 'credit'}]"
# print(type(tags))
# <class 'str'>
arr = list(np.array(tags))
# print(type(tags))
# <class 'numpy.ndarray'>
# print(tags)
# [{'thirdParty': 'Funds Transfer'}, {'category': 'External Transfers'}, {'creditDebit': 'credit'}]
for d in arr:
    print(d)