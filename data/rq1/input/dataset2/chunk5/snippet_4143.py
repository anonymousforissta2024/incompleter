#Source: https://stackoverflow.com/questions/55587722/stuck-with-typeerror-cannot-compare-types-ndarraydtype-object-and-str
cols = ['Keyword']

for col in cols:
    val = df_ch[col].value_counts()
    y = val[val < 10000].index

df_ch[col] = df_ch[col].replace({x:'other' for x in y})