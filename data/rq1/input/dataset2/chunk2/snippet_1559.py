#Source: https://stackoverflow.com/questions/33684848/typeerror-strptime-argument-0-must-be-str-not-class-bytes
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from datetime import datetime

days, impressions = np.loadtxt("page-impressions.csv", unpack=True,
        converters={ 0: mdates.strpdate2num('%Y-%m-%d')})

plt.plot_date(x=days, y=impressions, fmt="r-")
plt.title("Pageessions on example.com")
plt.ylabel("Page impressions")
plt.grid(True)

plt.savefig('test.pdf', format='pdf')