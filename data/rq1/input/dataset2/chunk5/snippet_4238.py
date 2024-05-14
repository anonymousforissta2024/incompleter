#Source: https://stackoverflow.com/questions/53086733/attribute-error-in-python-setting-y-ticks-to-minutes
from matplotlib.dates import MinuteLocator

fig, ax = plt.subplots(figsize=(10, 6))
ax.yaxis.set_major_formatter(MinuteLocator())
ax.bar(df.x, df['time_minutes'], width=25, align='center')