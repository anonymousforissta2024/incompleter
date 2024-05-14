#Source: https://stackoverflow.com/questions/75388748/typeerror-read-excel-got-an-unexpected-keyword-argument-dtype
import pandas as pd
data = pd.read_excel('sheet_path', 'sheet_name', dtype={'col1':str})