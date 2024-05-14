#Source: https://stackoverflow.com/questions/21886641/printout-typeerror-bool
import win32com.client

ExObj = win32com.client.Dispatch("Excel.Application")
ExObj.Visible = 1
wb = ExObj.Workbooks.Open('')
ws = wb.Worksheets[0]
ws.printout()