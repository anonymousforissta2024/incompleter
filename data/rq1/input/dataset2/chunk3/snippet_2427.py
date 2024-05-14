#Source: https://stackoverflow.com/questions/59391797/pandas-typeerror-data-type-not-understood
df_1['Vendor Number'].replace('', np.NAN, inplace=True)
df_1['Vendor Number'].replace('"', '', inplace=True)
df_1['Vendor Number'].dropna(inplace=True)

df_2['Artikel_Nummer'].replace('', np.NAN, inplace=True)
df_2['Artikel_Nummer'].replace('"', '', inplace=True)
df_2['Artikel_Nummer'].dropna(inplace=True)  