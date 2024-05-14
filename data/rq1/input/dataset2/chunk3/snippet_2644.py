#Source: https://stackoverflow.com/questions/70777905/str-attribute-error-when-using-apply-on-a-pandas-series
df['Unspent']=df.apply(unspent,axis=1)