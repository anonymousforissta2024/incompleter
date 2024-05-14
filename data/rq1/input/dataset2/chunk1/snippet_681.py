#Source: https://stackoverflow.com/questions/48348803/typeerror-not-supported-between-instances-of-int-and-list-in-numpy-inte
phone=df_final_naFill.iloc[0,4]
type(phone) # List
s=pd.Series(phone)
type(s) #pandas.core.series.Series
a=pd.Series(s.apply(pd.Series).stack().astype(int).groupby(level=0).apply(list))
phone_office=df_final_naFill.iloc[0,6]
# type(phone_office) #List
h=pd.Series(phone_office)
phone_comb=np.intersect1d(a,h)