#Source: https://stackoverflow.com/questions/54870178/attributeerror-when-trying-to-save-pandas-dataframe-to-existing-excel-sheet
path = 'summary.xlsx'
book = load_workbook(path)
writer = pd.ExcelWriter(path, engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

df.to_excel(writer, sheet_name="results")
writer.save()