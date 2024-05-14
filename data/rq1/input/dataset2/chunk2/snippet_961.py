#Source: https://stackoverflow.com/questions/70987659/getting-typeerror-string-indices-must-be-integers-error-while-iterating-dataf
data=[]
for i in df.iterrows():
    data.append({
       'c': i['country'],
       'v': i['value']
    })