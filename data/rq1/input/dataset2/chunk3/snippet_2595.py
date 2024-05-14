#Source: https://stackoverflow.com/questions/48592965/attributeerror-module-peakutils-has-no-attribute-indexes
import pandas as pd
import peakutils
from peakutils import *
import matplotlib.pyplot as plt

estimated_data = pd.read_csv("file", header=None)
col1 = estimated_data[:][0]  # First column data
col2 = estimated_data[:][1]  # Second column data

index = peakutils.indexes(col2, thres=0.4, min_dist=1000)

plt.plot(col1, col2, lw=0.4, alpha=0.4)
plt.plot(col1[index], col2[index], marker="o", ls="", ms=3)

plt.show()