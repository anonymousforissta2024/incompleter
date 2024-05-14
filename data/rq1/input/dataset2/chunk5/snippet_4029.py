#Source: https://stackoverflow.com/questions/60826193/type-error-while-writing-header-to-a-file-python3
import csv
import requests
from bs4 import BeautifulSoup

url='http://www.mapsofindia.com/districts-india/'
response=requests.get(url)
html=response.content

soup=BeautifulSoup(html,'html.parser')
table=soup.find('table', attrs={'class':'tableizer-table'})
list_of_rows=[]
for row in table.findAll('tr')[1:]:
    list_of_cells=[]
    for cell in row.findAll('td'):
        list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)
outfile=open('./immates.csv','wb')
writer=csv.writer(outfile)
writer.writerow(["SNo", "States", "Dist", "Population"])
writer.writerows(list_of_rows)