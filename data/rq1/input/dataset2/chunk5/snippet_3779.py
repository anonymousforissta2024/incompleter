#Source: https://stackoverflow.com/questions/49552931/typeerror-when-sqlalchemy-engine-connect-tries-to-compare-ms-sql-server-version
from sqlalchemy import create_engine
import pyodbc

engine = create_engine("mssql+pyodbc://user:pass@mydsn", echo=True)
cnxn = engine.connect()
rows = cnxn.execute("SELECT name FROM sys.tables").fetchall()
print(rows)