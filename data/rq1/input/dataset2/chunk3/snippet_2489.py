#Source: https://stackoverflow.com/questions/70777905/str-attribute-error-when-using-apply-on-a-pandas-series
data = {'Internal':  ['unpaid second interator 4,000 USD and $50 third', '35 $ unpaid', "all good"],
        'Name': ['Charlie', 'Rodolf', 'samuel']}

df = pd.DataFrame(data)

print (df)