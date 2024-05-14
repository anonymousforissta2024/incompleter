#Source: https://stackoverflow.com/questions/39069353/filenotfounderror-pointing-to-the-wrong-drive-letter-using-pythons-df2gspread
from df2gspread import df2gspread as d2g
import pandas as pd

df = live_data()
spreadsheet = 'my_spreadsheet_key'
wks_name = 'my_sheet_name'
d2g.upload(df, spreadsheet, wks_name)