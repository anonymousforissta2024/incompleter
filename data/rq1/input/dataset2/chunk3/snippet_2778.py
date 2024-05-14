#Source: https://stackoverflow.com/questions/52197977/issue-in-passing-an-array-to-an-index-in-series-objecttypeerror-len-of-unsiz
univals = set(a)
serObj=pd.Series()

for ele in univals:
    indexfound=np.where(a == ele)
    Xpointsfromindex=np.take(b, indexfound)
    serobj1=pd.Series(Xpointsfromindex[0],index=ele)   ##error happening here
    serObj.apend(serobj1)
print(serObj)