#Source: https://stackoverflow.com/questions/61996710/labelencoder-typeerror-argument-must-be-a-string-or-number
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
pd.set_option('display.max_columns', 500)
df=pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/831JKKEkW7kqd5M4evNva9LyB/insurance_grouped.csv")
le = LabelEncoder()#use this encoder to encod
df.BMI_group = le.fit_transform(df.BMI_group.values)
print(df.head())