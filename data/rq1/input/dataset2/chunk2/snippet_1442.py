#Source: https://stackoverflow.com/questions/56513526/attributeerror-function-object-has-no-attribute-summary
y=dataset
X=dataset [['A'] + ['B'] + ['C'] + ['D'] + ['E']]
X1 = sm.add_constant(X)
model = sm.OLS(endog = y, exog = X)
results = model.fit
results.summary()