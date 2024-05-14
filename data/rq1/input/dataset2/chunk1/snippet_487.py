#Source: https://stackoverflow.com/questions/36329269/python-legend-attribute-error
fig = plt.figure()
ax = plt.gca()
barplt = plt.bar(bins,frq,align='center',label='Dgr')
normplt = plt.plot(bins_n,frq_n,'--r', label='Norm');
ax.set_xlim([min(bins)-1, max(bins)+1])
ax.set_ylim([0, max(frq)])
plt.xlabel('Dgr')
plt.ylabel('Frequency')
plt.show()
plt.legend(handles=[barplt,normplt])