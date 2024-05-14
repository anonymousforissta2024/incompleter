#Source: https://stackoverflow.com/questions/41422386/python-3-5-2-openpyxl-v-2-4-1-get-highest-row-attributeerror
WorkBook = openpyxl.load_workbook("G:\\Python_Created\\DS.xlsx")
#I have a Sheet named "Original" in my Excell Workbook
Sheet = WorkBook.get_sheet_by_name("Original")
Sheet.get_highest_row()