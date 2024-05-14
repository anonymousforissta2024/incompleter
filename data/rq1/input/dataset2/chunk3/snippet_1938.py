#Source: https://stackoverflow.com/questions/69658815/typeerror-to-csv-got-an-unexpected-keyword-argument-startrow
def mokacsv(file_name):
    importing = pd.read_csv(file_name)
    column_netsales = importing['Net Sales']
    sum_of_netsales = (column_netsales)
    sum_of_netsales.to_csv('example1.csv', index=False, header=True, startrow=30)



print(mokacsv(r"example2.csv"))