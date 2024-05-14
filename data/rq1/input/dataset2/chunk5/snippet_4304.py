#Source: https://stackoverflow.com/questions/55324792/nameerror-name-dates-is-not-defined
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('tcs.csv', index_col = 'Date', parse_dates = True)

idx = df1.loc['2019-01-01':'2019-02-01'].index
stk = df1.loc['2019-01-01':'2019-02-01']['Close Price']

fig,ax =plt.subplots()
ax.plot_date(idx,stk,'-')

# ax.xaxis.grid(True)
# ax.yaxis.grid(True)

ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter("%b-%y"))

fig.autofmt_xdate()
plt.tight_layout()