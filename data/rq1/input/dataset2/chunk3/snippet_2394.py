#Source: https://stackoverflow.com/questions/47251752/matplotlib-pyplot-hist-attribute-error
import matplotlib.pyplot as plt
import numpy as np


test = [np.random.randn() for i in range(100)]

plt.hist(test)
plt.show()