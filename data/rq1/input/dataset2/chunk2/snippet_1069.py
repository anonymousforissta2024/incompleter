#Source: https://stackoverflow.com/questions/64940395/typeerror-read-excel-got-an-unexpected-keyword-argument-parse-cols
import numpy as np
import pandas as pd

url = 'https://www.dropbox.com/s/yze3laidhv7gl1x/Homework4.xlsx?dl=1'

changedate = lambda x: pd.to_datetime(x, format = "%Y%m") 

df = pd.read_excel(url, sheet_name = '49_Industry_Portfolios', header = 6, 
                   parse_cols = 'AZ:CW', index_col = 0, parse_dates = True, 
                   date_parser = changedate, na_values = [-99.99, -999])
print(df)