import numpy as np
a = np.arange(1, 11)
sqrtFive = np.sqrt(5)
alpha = (1 + sqrtFive) / 2
beta = (1 - sqrtFive) / 2
Fn = np.rint((alpha ** a - beta ** a) / sqrtFive)
print('The first {} numbers of Fibonacci series are {} . '.format(lengthA, Fn))