#Source: https://stackoverflow.com/questions/39141466/python-2-7-typeerror-float-object-has-no-attribute-getitem
import numpy as np
import matplotlib.pyplot as plt

a = 0.75 + (1.25 - 0.75)*np.random.lognormal(10000)

[n,bins,patches] = plt.hist(a, bins=50, color = 'red',alpha = 0.5, normed = True)

plt.show()