#Source: https://stackoverflow.com/questions/60078342/pandas-read-sql-query-throws-typeerror-nonetype-object-is-not-iterable
@contextmanager
def open_db_connection(connection_string):
    pyodbc.pooling = False
    connection = pyodbc.connect(connection_string)

    try:
        yield connection
    except pyodbc.DatabaseError as err:
        error, = err.args
        sys.stderr.write(error.message)
    finally:
        connection.close()

noCount = """ SET NOCOUNT ON; """
with open_db_connection(connection_string) as conn:
    res = pd.read_sql_query(noCount+queryObj, conn)