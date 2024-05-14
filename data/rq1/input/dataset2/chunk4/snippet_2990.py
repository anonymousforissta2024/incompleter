#Source: https://stackoverflow.com/questions/66610488/correlation-in-pandas-attributeerror-float-object-has-no-attribute-shape
dfCorrelation=pd.read_csv(filename)
df1 = dfCorrelation.loc[1] #to subset the first row
df2 = dfCorrelation.loc[2] #to subset the second row
print(df1.corr(df2))