#Source: https://stackoverflow.com/questions/58116673/fuzzy-string-matching-with-pandas-and-fuzzywuzzy-data-matching-typeerror-canno
import pandas as pd


names_array=[]
ratio_array=[]
def match_names(wrong_names,correct_names):
    for row in wrong_names:
        x=process.extractOne(row, correct_names)
        names_array.append(x[0])
        ratio_array.append(x[1])
    return names_array,ratio_array

fields = ['name']
#Wrong country names dataset
df=pd.read_csv("wrong-country-names.csv",encoding="ISO-8859-1",sep=';', skipinitialspace=True, usecols= fields )
print(df.dtypes)


wrong_names=df.dropna().values


#Correct country names dataset
choices_df=pd.read_csv("country-names.csv",encoding="ISO-8859-1",sep='\t', skipinitialspace=True)
correct_names=choices_df.values

name_match,ratio_match=match_names(wrong_names,correct_names)

df['correct_country_name']=pd.Series(name_match)
df['country_names_ratio']=pd.Series(ratio_match)

df.to_csv("string_matched_country_names.csv")

print(df[['name','correct_country_name','country_names_ratio']].head(10))