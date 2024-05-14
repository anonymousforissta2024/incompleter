#Source: https://stackoverflow.com/questions/65552218/how-to-fix-attributeerror-nonetype-object-has-no-attribute-locpandas
import pandas as pd

data = pd.read_csv('sample.csv',delimiter=',')

def mapping(df):
     #work of data mapping
     for column_name, column in df.transpose().iterrows():
         df.rename(columns ={'first name' : 'FNAME', 'secret': 'CODE'}, inplace = True)
         df.rename(columns ={'alias' : 'FNAME', 'code': 'CODE'}, inplace = True)
         df.rename(columns ={'initial name' : 'FNAME', 'id': 'CODE'}, inplace = True)

final_df = mapping(data)

#If the code is greater than 12 digits, leave it blank
final_df.loc[final_df['CODE'].astype(str).str.len() >12, 'CODE']= ''