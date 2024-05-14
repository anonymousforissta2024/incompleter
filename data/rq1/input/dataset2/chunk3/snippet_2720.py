#Source: https://stackoverflow.com/questions/57998473/np-vectorize-for-typeerror-only-size-1-arrays-can-be-converted-to-python-scalar
import numpy as np
import math


S0 = 50

k_list = np.linspace(S0 * 0.6, S0 * 1.4, 50)

K=k_list

d1 = np.vectorize(math.log(S0 / K))

print(d1)