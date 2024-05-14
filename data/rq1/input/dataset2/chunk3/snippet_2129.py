#Source: https://stackoverflow.com/questions/69051693/is-attributeerror-working-as-it-should-pandas-df
"""
creating dict of {symbol:[spot, aggregate]
"""

abn_dict = defaultdict(lambda: [0, 0])

for (col, row) in abn_df.iterrows():
    try:
        row.loc["Quantity Long"].isnull()
        abn_dict[row.loc["Symbol"]][1] += row.loc["Quantity Short"]
    except AttributeError:
        abn_dict[row.loc["Symbol"]][1] += row.loc["Quantity Long"]