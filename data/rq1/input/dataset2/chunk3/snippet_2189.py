#Source: https://stackoverflow.com/questions/62502168/querying-float-to-filter-a-pandas-dataframe-get-typeerror-not-supported-bet
temp = df.query("temp" > 10.00, inplace = True)