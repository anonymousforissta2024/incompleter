#Source: https://stackoverflow.com/questions/76864344/spire-xls-for-python-produces-attributeerror-nonetype-object-has-no-attribute
from spire.xls import *
from spire.common import *


inputFile = "/Users/myname/Desktop/XYZ.xlsm"
outputFile = "/Users/myname/Library/Mobile      Documents/com~apple~CloudDocs/Development/CellRangeToPDF.pdf"

#create a workbook
workbook = Workbook()
#load a excel document
workbook.LoadFromFile(inputFile)
workbook.ConverterSetting.SheetFitToPage = True
#convert to PDF file
workbook.SaveToFile(outputFile, FileFormat.pdf)
workbook.Dispose()