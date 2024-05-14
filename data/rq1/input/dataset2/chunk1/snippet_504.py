#Source: https://stackoverflow.com/questions/60280466/merging-two-dataframes-with-pd-na-in-merge-column-yields-typeerror-boolean-val
df[some_column].fillna(np.nan, inplace=True)
df2[some_column].fillna(np.nan, inplace=True)
df = df.merge(df2, on=some_column)
# Works