#Source: https://stackoverflow.com/questions/70081820/ibm-as400-file-not-found-error-while-the-table-object-is-still-there
import pyodbc

connection = pyodbc.connect(
    Driver='{iSeries Access ODBC Driver}',
    System='<host>',
    database='<database>',
    uid='<username>',
    pwd='<password>')
c1 = connection.cursor()
print('Connection established')