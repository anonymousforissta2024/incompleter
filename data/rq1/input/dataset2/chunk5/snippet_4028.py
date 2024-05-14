#Source: https://stackoverflow.com/questions/58458756/pyodbc-type-error-the-first-argument-to-execute-must-be-a-string-or-unicode-q
import pyodbc 
import pandas as pd 

conn = pyodbc.connect(
                      'DRIVER={SQL Server};'
                      'SERVER=192.168.1.30;'
                      'DATABASE=Datamart;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor() 
for row in cursor.tables(tableType='TABLE'): 
    print(row)
sql = """SELECT * FROM ETL.Dim_FC_UPS_Interface_Detail"""
cursor.execute(row, sql)

df = pd.read_sql(sql, conn)
df.head()