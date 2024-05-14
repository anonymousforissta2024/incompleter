#Source: https://stackoverflow.com/questions/59185633/typeerror-object-of-type-map-has-no-len-when-trying-to-insert-a-csv-into-an
import csv  
import pyodbc  

thecsv = 'iamacsvfile.csv'

print('connecting')
drivr = "SQL Server"
servr = "1.2.3.4"
db = "testdata"
username = "user"
password = "thepassword"
my_cnxn = pyodbc.connect('DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(drivr,servr,db,username,password))

my_cursor = my_cnxn.cursor()

def insert_records(table, thecsv, my_cursor, my_cnxn):

    with open(thecsv) as csvfile:
        csvFile = csv.reader(csvfile, delimiter=',')
        header = next(csvFile)
        headers = map((lambda x: x.strip()), header)
        insert = 'INSERT INTO {} ('.format(table) + ', '.join(headers) + ') VALUES ({})' .format(', '.join(len(headers) * '?'))
        for row in csvFile:
            values = map((lambda x: x.strip()), row)  
            my_cursor.execute(insert, values) 
            my_cnxn.commit()


table = 'dbo.iamthetable'
mycsv = thecsv 
insert_records(table, mycsv, my_cursor, my_cnxn)
my_cursor.close()