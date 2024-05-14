#Source: https://stackoverflow.com/questions/62502168/querying-float-to-filter-a-pandas-dataframe-get-typeerror-not-supported-bet
df.temp = pd.to_numeric(df.temp,  errors='coerce')