#Source: https://stackoverflow.com/questions/41138148/pandas-to-sql-incorrect-column-name-error
data.to_sql('sample_table',mysql_engine, if_exists= 'replace', index = False)