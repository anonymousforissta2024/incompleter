#Source: https://stackoverflow.com/questions/54585333/typeerror-bad-operand-type-for-unary-float
df.REFERENCE_CODE = df.REFERENCE_CODE.fillna('')

df.REFERENCE_CODE.str.isnumeric().dtype # returns object

headers = (df.REFERENCE_CODE != '') & ~df.REFERENCE_CODE.str.isnumeric()

res = df.groupby(headers.cumsum())['REFERENCE_CODE'].apply(lambda x: x.iloc[0] + '_' + x)

df.REFERENCE_CODE.update(res[df.REFERENCE_CODE.str.isnumeric()])