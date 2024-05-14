#Source: https://stackoverflow.com/questions/39767292/unhashable-type-error-list
text = pd.read_sql(select_string, con)
ftext = text['SomeText'].str.split()
country_codes = pd.read_csv('wikipedia-iso-country-codes.csv')
ccs = set(country_codes['English short name lower case'])
for country in ftext:
    if country in ccs:                  #this is where the error occurs
       print(country+'  is in the text')