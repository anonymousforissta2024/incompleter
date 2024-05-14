#Source: https://stackoverflow.com/questions/60443038/pandas-date-range-query-gives-typeerror-series-objects-are-mutable-thus-the
df_contracts = read_csv("_raw_contracts.csv")
df_contracts['Start'] = pd.to_datetime(df_contracts['Start'])
df_contracts['End'] = pd.to_datetime(df_contracts['End'])
anchor = pd.Timestamp('2010-01-01T12')
df = df_contracts.loc(df_contracts['Start'] < anchor) & (df_contracts['End'] > anchor)