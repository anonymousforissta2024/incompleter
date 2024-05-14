#Source: https://stackoverflow.com/questions/50060699/matplotlib-typeerror-unsupported-operand-types-for-datetime-date-and-fl
import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

DF = pd.DataFrame({
    'day':     [datetime(2018,1,1).date()+timedelta(x+1) for x in range(100)],
    'balance': np.random.normal(100,100,100)
})
rcParams['figure.figsize'] = 20, 10
fig, ax = plt.subplots()
ax.bar(DF['day'], DF['balance'], color='lightblue')
plt.xlabel('day', fontsize=20)
myFmt = mdates.DateFormatter('%Y-%m')
ax.xaxis.set_major_formatter(myFmt)
plt.show()