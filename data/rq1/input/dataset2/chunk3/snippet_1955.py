#Source: https://stackoverflow.com/questions/74920325/dtreeviz-attributeerror-dataframe-object-has-no-attribute-dtype-python
X = df1[['age', 'gender', 'portfolio_type', 'platform']]
X = pd.get_dummies(data=X, drop_first=True)

Y = df1[[ 'Customer']]
Y = pd.get_dummies(data=Y, drop_first=True)