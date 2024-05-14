import numpy as np
y = np.array([4, 5])
result = np.transpose([np.tile(x, len(y)), np.repeat(y, len(x))])
print(result)