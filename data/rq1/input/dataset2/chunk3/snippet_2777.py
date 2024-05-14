#Source: https://stackoverflow.com/questions/53203046/dont-know-why-attributeerror-list-object-has-no-attribute-groupby
df = pd.read_csv('e:/test_csv', low_memory=False)

data1 = a.groupby('ta')['income'].sum()
data1.plot.pie(autopct='%.1f%%')

data2 = a.groupby('tb')['income'].sum()
data2.plot.pie(autopct='%.1f%%')

data3 = a.groupby('tc')['income'].sum()
data3.plot.pie(autopct='%.1f%%')

plt.show()