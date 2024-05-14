#Source: https://stackoverflow.com/questions/63065832/matplotlib-using-twinx-typeerror-axessubplot-object-does-not-support-item
fig, ax = plt.subplots(4,5,figsize=(8,8))
ax2=ax.twinx()