#Source: https://stackoverflow.com/questions/46582490/typeerror-ufunc-add-did-not-contain-a-loop-with-signature-for-arima-model
Cdx = CpcGDP.columns[0]
S = CpcGDP.loc[:, Cdx]
S.astype(float)