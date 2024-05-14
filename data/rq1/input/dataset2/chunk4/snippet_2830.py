#Source: https://stackoverflow.com/questions/61252498/attributeerror-can-only-use-dt-accessor-with-datetimelike-values-while-tryin
df['weekday'] = df['Date'].dt.dayofweek