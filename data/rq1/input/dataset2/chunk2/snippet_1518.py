#Source: https://stackoverflow.com/questions/48120611/python-pandas-filtering-typeerror-cannot-convert-the-series-to-class-int
DF[(DF.Instrument=='WTICO_USD')&(int(DF['Units'])>-1)]