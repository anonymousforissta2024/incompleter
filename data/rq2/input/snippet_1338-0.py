import numpy as np
import matplotlib.pyplot as plt
y, x = np.histogram(arr, bins=np.arange(51))
fig, ax = plt.subplots()
ax.plot(x[:-1], y)
fig.show()