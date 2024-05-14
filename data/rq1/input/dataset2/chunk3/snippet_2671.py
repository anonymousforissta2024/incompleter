#Source: https://stackoverflow.com/questions/66302949/pandas-to-sql-typeerror-unsupported-operand-type
df = pd.read_csv("test_repositories.csv", 
        header=0, 
        sep=',',
        quotechar='"',
        dtype={'column_one': str,
            'column_two': str,
            'column_three': str,
            'column_four': int},
            error_bad_lines=False)
df = df.where(pd.notnull(df), None)
df.to_sql(self.staging_table, db.engine, self.chunksize, method='multi')