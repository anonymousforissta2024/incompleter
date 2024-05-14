#Source: https://stackoverflow.com/questions/30782676/attributeerror-exit-on-python-3-4
import sys
import os
import latexmake

import mysql.connector
conn = mysql.connector.connect(user='root',password='oilwell',host='localhost',database='sqlpush1')

with conn:
    mycursor = conn.cursor()
mycursor=execute("SELECT DATE,oil,gas,oilprice,gasprice,totrev FROM results WHERE DATE BETWEEN '2011-01-01' AND '2027-12-01'")
rows = mycursor.fetchall()
a.write("\\documentclass{standalone}\\usepackage{booktabs}\n\n\\usepackage{siunitx}\r \n\
\r\n\\begin{document}\r\n\\begin{tabular}{ccS[table-format = 5.2]} \\\\ \\toprule\r")
a.write("Date & Oil & Gas & Oil price & Gas price & Total Revenue \\\\ \\midrule \r")
for row in rows:
    a = open("testtest.tex", "w")
    a.write("" + str(row[0]) + " & " + str(row[1]) + " & " + str(row[2]) + " & " + str(row[3]) + " & " + str(row[4]) + " & " + str(row[5]) + " \\\\ \r")

    a.write("\\bottomrule \\end{tabular}\r\\end{document}")
    a.close
print (os.path.getsize("testtest.tex"))
os.system('latexmk.py -q testtest.tex')
mycursor.close()
conn.close()
a.close()