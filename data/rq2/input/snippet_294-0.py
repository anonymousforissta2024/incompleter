import numpy as np
n = x[(x % 3 == 0) | (x % 5 == 0)]
print(n[:1000])
print(n.sum())