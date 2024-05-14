#Source: https://stackoverflow.com/questions/56119642/is-there-a-solution-for-attributeerror-nonetype-object-has-no-attribute-wor
import openpyxl

wb = openpyxl.load_workbook('test1.xlsx' )

wb.security.workbookPassword.value = 'test_password'
wb.security.lockStructure = True