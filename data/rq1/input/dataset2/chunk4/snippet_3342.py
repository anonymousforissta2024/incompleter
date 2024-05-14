#Source: https://stackoverflow.com/questions/74099141/attributeerror-nonetype-object-has-no-attribute-set-column
wb = xlsx.Workbook(File_path)
ws = ws 

ws.set_column('A:A', 60)