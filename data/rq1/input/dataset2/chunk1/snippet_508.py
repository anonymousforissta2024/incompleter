#Source: https://stackoverflow.com/questions/53307308/statmodels-ols-giving-a-typeerror-in-python
new_df0 = pd.concat([df_len[0], summary_df[0]], axis = 0, join = 'inner')
new_df1 = pd.concat([df_len[1], summary_df[1]], axis = 0, join = 'inner')

data = pd.concat([new_df0, new_df1], axis = 1)
print(data.shape)
X = data.values[0:2,:]
Y = data.values[2,:]
Y = Y.reshape(1,88)
X = X.T
Y = Y.T
X = X.astype(float)
print(X.shape)
print(Y.shape)

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)
print(model.summary())