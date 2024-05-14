#Source: https://stackoverflow.com/questions/41738636/typeerror-while-calling-pandas-excelfile
pd.read_excel(io.open(encoding=sys.getfilesystemencoding()))