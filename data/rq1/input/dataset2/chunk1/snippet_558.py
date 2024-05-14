#Source: https://stackoverflow.com/questions/48669373/invalid-column-name-error-when-writing-pandas-dataframe-to-sql
cnxn = sqlalchemy.create_engine("mssql+pyodbc://@HOST:PORT/DATABASE?driver=SQL+Server") 
df.to_sql('DATABASE.dbo.TABLENAME', cnxn, if_exists='append', index=False)