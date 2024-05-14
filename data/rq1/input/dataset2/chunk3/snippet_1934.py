#Source: https://stackoverflow.com/questions/49154068/fixing-a-typeerror-when-using-pandas-after-replacing-a-string-with-a-floating-po
wt.groupby(wt.index.month)['Precip'].sum().plot(kind='bar')