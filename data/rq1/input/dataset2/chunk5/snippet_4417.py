#Source: https://stackoverflow.com/questions/62576200/filenotfounderror-python
if boolErrorsOnly :
    mfile = "NewPayrollExports\Admin_ErrorsOnly_" + m0weekbeg + "_" + m0weekend + ".csv"
else:
    mfile = "NewPayrollExports\\Admin_" + m0weekbeg + "_" + m0weekend+".csv"

#Copy the field list to csv file
with open(mfile,'r+', newline='') as mhvupload_csv:
    writer = csv.writer(mhvupload_csv)
    writer.writerow(strFieldList)