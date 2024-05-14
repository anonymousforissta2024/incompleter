#Source: https://stackoverflow.com/questions/49154068/fixing-a-typeerror-when-using-pandas-after-replacing-a-string-with-a-floating-po
wt2 = wt[['Precip']]

wt2.astype(float)

wt2.groupby(wt2.index.month)['Precip'].sum().plot(kind='bar')