#Source: https://stackoverflow.com/questions/50119668/attributeerror-generator-object-has-no-attribute-to-sql-while-creating-datf
import pandas.io.sql as psql
import pandas as pd
from sqlalchemy import create_engine

def chunck_generator(filename, header=False,chunk_size = 10 ** 5):
    for chunk in pd.read_fwf(filename, colspecs=[[0,12],[12,13]],index_col=False,header=None, iterator=True, chunksize=chunk_size):
        yield (chunk)

def _generator( engine, filename, header=False,chunk_size = 10 ** 5):
    chunk = chunck_generator(filename, header=False,chunk_size = 10 ** 5)
    chunk.to_sql('sample_table', engine, if_exists='replace', schema='sample_schema', index=False)
    yield row

if __name__ == "__main__":
    filename = r'test_file.txt'
    engine = create_engine('postgresql://ABCD:ABCD@ip:port/database')
    c = engine.connect()
    conn = c.connection
    generator = _generator(engine=engine, filename=filename)
    while True:
       print(next(generator))
    conn.close()