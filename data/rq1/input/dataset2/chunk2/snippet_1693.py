#Source: https://stackoverflow.com/questions/69648331/unable-to-load-workbook-typeerror-expected-class-openpyxl-chart-axis-numeri
import openpyxl

wb = openpyxl.load_workbook('test.xlsm', data_only=True)
sheets = wb.sheetnames
x = wb[sheets[0]]