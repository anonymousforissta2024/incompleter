#Source: https://stackoverflow.com/questions/54202579/type-error-when-trying-to-modify-values-using-loc
df = df.assign(e=pd.Series(np.random.randn(len(df))).values)