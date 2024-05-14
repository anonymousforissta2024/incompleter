#Source: https://stackoverflow.com/questions/58443969/getting-typeerror-fit-missing-1-required-positional-argument-self
lm = LinearRegression

x = df[['battery_power']]

y = df['price']

lm.fit(X=x, y=y)