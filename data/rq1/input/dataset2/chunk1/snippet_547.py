#Source: https://stackoverflow.com/questions/60280466/merging-two-dataframes-with-pd-na-in-merge-column-yields-typeerror-boolean-val
df[some_column].fillna(pd.NA, inplace=True)