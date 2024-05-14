#Source: https://stackoverflow.com/questions/60649173/numpy-typeerror-ufunc-bitwise-and-not-supported-for-the-input-types
condition = [((df_merge['column1'] == 'a') & (df_merge['column2'] == df_merge['column2'].isin(bb))),((df_merge['column1'] == 'c') & (df_merge['column2'] == df_merge['column2'].isin(dd))), ((df_merge['column1'] == 'e') & (df_merge['column2'] == df_merge['column2'].
isin(ff)))]

choices1 = [((np.where(df_merge['column3'] >= 1, 'should not have, ','correct')) & (np.where(df_merge['column4'] >= 0.45, 'should not have, ','correct')))]

df_merge['Reason'] = np.select(condition, choices1, default='correct')