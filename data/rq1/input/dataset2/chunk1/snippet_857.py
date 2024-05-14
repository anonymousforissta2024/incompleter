#Source: https://stackoverflow.com/questions/61584592/python3-typeerror-generator-object-is-not-subscriptable
import sys
import numpy as np
from scipy import stats

max_event = 1000000
a_bin = 10  # number each bin from 0-->10 where cumulant calculation will be done

# Define 2D array for [ bin, here 0->10][proton in each bin]
pArray = (() for nn in range(a_bin))
neve = (0 for mm in range(a_bin))

for ii in range(0, max_event):

    _a = np.random.randint(10)
    _b = np.random.randint(120)

    if ii % 1000 == 0:
        print(ii, _a, _b)

    for j in range(0, 10):
        if _a == j:
            pArray[j].append(_b)
            neve[j] += 1


print("filling done!")

for k in range(0, a_bin):

    mu2 = stats.mstats.moment(pArray[k], moment=2)
    mu4 = stats.mstats.moment(pArray[k], moment=4)

    print('serial = %d, mu_2 = %f , mu_4 = %f, event = %d' %
          (k, mu2, mu4, neve[k]))
    # print k, neve[k], c1[k], c2[k], c3[k], c4[k], c5[k], c6[k]

print("calculation done!")