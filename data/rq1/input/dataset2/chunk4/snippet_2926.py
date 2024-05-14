#Source: https://stackoverflow.com/questions/77152839/reason-attributeerror-can-only-use-dt-accessor-with-datetimelike-values
import pandas as pd
file = '/pathtocsv.csv'
df = pd.read_csv(file, sep = ',', encoding='utf-8-sig', usecols= ['Date', 'ids'])    
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month