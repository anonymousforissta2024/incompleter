#Source: https://stackoverflow.com/questions/75756305/attributeerror-pandasexprvisitor-error-when-trying-to-optimize-pandas-p
df["v1"] = df.apply(lambda row: row['col3':'col5'].tolist(), axis=1)
df["v2"] = df.apply(lambda row: row['col6':'col8'].tolist(), axis=1)
v1 = df['v1'].to_numpy()
v2 = df['v2'].to_numpy()

# check if current value in column A is equal to any other values in column A
mask_A_A = pd.eval('v1[:, None] == v1')

# check if current value in column A is equal to any other values in column B
mask_A_B = pd.eval('v1[:, None] == v2')

# check if current value in column B is equal to any other values in column B
mask_B_B = pd.eval('v2[:, None] == v2')

# check if any values in column B is equal to any other values in column A
mask_B_A = pd.eval('v2[:, None] == v1')

# combine masks and use numexpr to create col9 column
mask = ne.evaluate(
        '(mask_A_A | mask_A_B | mask_B_B | mask_B_A) & (v1[:, None] != v1) & (v2[:, None] != v2)')
col9 = np.where(mask, df['col2'].values[:, None], '')
df['col9'] = pd.Series([', '.join(names) if len(names) > 0 else None for names in col9])