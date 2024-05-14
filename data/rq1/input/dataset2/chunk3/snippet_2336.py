#Source: https://stackoverflow.com/questions/68603734/pandas-error-typeerror-bad-operand-type-for-unary-float
dummy_data1 = {
    'id': ['1', '2', '3', '4', '5'],
    'Feature1': ['A', 'C', 'E', 'G', 'I'],
    'Feature2': ['Mouse', 'dog', 'house and parrot', '23', np.NaN],
    'dates': ['12/12/2020','12/12/2020','12/12/2020','12/12/2020','12/12/2020']}

df1 = pd.DataFrame(dummy_data1, columns = ['id', 'Feature1', 'Feature2', 'dates'])

df1 = df1.assign(
                    Feature2=lambda df: df.Feature2.where(
                        ~df.Feature2.str.isnumeric(),
                        pd.to_numeric(df.Feature2, errors="coerce").astype("Int64"),
                    )
    )
    
print(df1)