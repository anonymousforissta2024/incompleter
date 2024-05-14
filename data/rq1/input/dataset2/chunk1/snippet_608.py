#Source: https://stackoverflow.com/questions/48669373/invalid-column-name-error-when-writing-pandas-dataframe-to-sql
df.to_sql('TABLENAME', cnxn, if_exists='append', index=False)