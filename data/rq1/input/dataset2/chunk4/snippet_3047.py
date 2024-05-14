#Source: https://stackoverflow.com/questions/34421005/mysql-date-range-pull-using-python-typeerrorunhashable-type-bytearray
# Establish a MySQL connection
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
db_config = read_db_config()
conn = MySQLConnection(**db_config)
cursor = conn.cursor(raw=True)

#to export to excel
import xlsxwriter
from xlsxwriter.workbook import Workbook

#to get the csv converter functions
import os
import subprocess
import glob

#to get the datetime functions
import datetime
from datetime import datetime
import dateutil.parser

#creates the path needed for output files
path = 'C:/Python34/output_files/'

#creates the workbook
output_filename = input('output filename:')
workbook = xlsxwriter.Workbook(path + output_filename + '.xlsx')
worksheet = workbook.add_worksheet()

#formatting definitions
bold    = workbook.add_format({'bold': True})
date_format = workbook.add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'})
timeShape =  '%Y-%m-%d %H:%M:%S'

#actual query


query = (
    "SELECT sent_time, delivered_time, OBJ, id1_active, id2_active, id3_active, id1_inactive, id2_inactive, id3_inactive, location_active, location_inactive FROM table1 "
    "WHERE sent_time BETWEEN %s AND %s"
)
userIn = dateutil.parser.parse(input('start date:'))
userEnd = dateutil.parser.parse(input('end date:'))


# Execute sql Query
cursor.execute(query,(userIn, userEnd))
result = cursor.fetchall()


#sets up the header row
worksheet.write('A1','sent_time',bold)
worksheet.write('B1', 'delivered_time',bold)
worksheet.write('C1', 'customer_name',bold)
worksheet.write('D1', 'id1_active',bold)
worksheet.write('E1', 'id2_active',bold)
worksheet.write('F1', 'id3_active',bold)
worksheet.write('G1', 'id1_inactive',bold)
worksheet.write('H1', 'id2_inactive',bold)
worksheet.write('I1', 'id3_inactive',bold)
worksheet.write('J1', 'location_active',bold)
worksheet.write('K1', 'location_inactive',bold)
worksheet.autofilter('A1:K1')  #dropdown menu created for filtering


#print into client to see that you have results
print("     sent_time     ", "        delivered_time     ", "OBJ", "\t   id1_active  ", "   id2_active  ", "    id3_active  ", "\t", " id1_inactive ", " id2_inactive ", "  id3_inactive ", "\tlocation_active", "\tlocation_inactive")
for row in result:
    print(*row, sep='\t')


# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r, row in enumerate(result, start=1):  #where you want to start printing results inside workbook
    for c, col in enumerate(row):
        worksheet.write_datetime(r,0,row[0], date_format)
        worksheet.write_datetime(r,1, row[1], date_format)
        worksheet.write(r,2, row[2])
        worksheet.write(r,3, row[3])
        worksheet.write(r,4, row[4])
        worksheet.write(r,5, row[5])
        worksheet.write(r,6, row[6])
        worksheet.write(r,7, row[7])
        worksheet.write(r,8, row[8])
        worksheet.write(r,9, row[9])
        worksheet.write(r,10, row[10])




#close out everything and save
cursor.close()
workbook.close()
conn.close()

#print number of rows and bye-bye message
print ("- - - - - - - - - - - - -")
rows = len(result)
print ("I just imported "+ str(rows) + " rows from MySQL!")
print ("")
print ("Good to Go!!!")
print ("")


#CONVERTS JUST CREATED FILE TO CSV

# set path to folder containing xlsx files

out_path ='C:/Python34/csv_files'
os.chdir(path)


# find the file with extension .xlsx
xlsx = glob.glob(output_filename + '.xlsx')

# create output filenames with extension .csv
csvs = [x.replace('.xlsx','.csv') for x in xlsx]

# zip into a list of tuples
in_out = zip(xlsx,csvs)

# loop through each file, calling the in2csv utility from subprocess
for xl,csv in in_out:
   out = open(csv,'w')
   command = 'c:/python34/scripts/in2csv %s\\%s' % (path,xl)
   proc = subprocess.Popen(command,stdout=out)
   proc.wait()
   out.close()

print('XLSX and CSV files named ' + output_filename + ' were created')