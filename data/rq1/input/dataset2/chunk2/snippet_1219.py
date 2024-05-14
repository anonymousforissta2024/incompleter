#Source: https://stackoverflow.com/questions/75756305/attributeerror-pandasexprvisitor-error-when-trying-to-optimize-pandas-p
df["v1"] = df.apply(lambda row: row['col3':'col5'].tolist(), axis=1)
df["v2"] = df.apply(lambda row: row['col6':'col8'].tolist(), axis=1)
v1 = df['v1'].to_numpy()
v2 = df['v2'].to_numpy()

m = (v1 == v1[:, None]) | (v2 == v2[:, None]) | (v1 == v2[:, None]) | (
            v2 == v1[:, None])

np.fill_diagonal(m, False)

df['col9'] = np.dot(m, df['col2'] + ',')
df['col9'] = df['col9'].str[:-1].replace('', np.nan, regex=True)