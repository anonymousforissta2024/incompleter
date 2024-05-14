#Source: https://stackoverflow.com/questions/48516372/getting-typeerror-during-creation-of-bar-chart-from-excel-using-openpyxl-referen
data =   Reference(wsheet, min_col=5, min_row=2, max_col=5, max_row=10)
categs = Reference(wsheet, min_col=3, min_row=2, max_col=3, max_row=10)