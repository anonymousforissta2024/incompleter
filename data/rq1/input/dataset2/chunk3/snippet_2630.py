#Source: https://stackoverflow.com/questions/58400635/typeerror-only-integer-scalar-arrays-can-be-converted-to-a-scalar-index-pandas
df2 = pd.merge(df1, toi_data, on=['Player', 'Team', 'Year'])