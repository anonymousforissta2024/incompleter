#Source: https://stackoverflow.com/questions/54480138/typeerror-parser-f-got-multiple-values-for-argument-sep
import pandas as pd

df = pd.read_csv(open('duplicate1.csv'),'Sheet1',sep=',',delimiter=None, index_col=0)

df.to_excel('duplicateexcel.xlsx',encoding='utf-8')