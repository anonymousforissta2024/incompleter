#Source: https://stackoverflow.com/questions/55887818/dataframe-operation-typeerror-cannot-convert-the-series-to-class-float
df  = pd.DataFrame([["Gothenburg", "2018-01-05", "jan", 1.5, 2.3, 107],
 ["Gothenburg", "2018-01-15", "jan", 1.3, 3.3, 96],
 ["Hallsberg", "2018-02-14", "feb", 2.2, 2.3, 168],
 ["Gothenburg", "2018-03-05", "mar", 1.5, 2.1, 96],
 ["Hallsberg", "2018-01-25", "jan", 2.5, 2.3, 87],
 ["Malmo", "2018-01-02", "jan", 1.6, 2.3, 104],
 ["Gothenburg", "2018-03-05", "mar", 1.9, 2.8, 102],
 ["Malmo", "2018-03-05", "mar", 0.7, 4.3, 151],
 ["Gothenburg", "2018-01-25", "jan", 1.7, 3.2, 45],
 ["Malmo", "2018-03-25", "mar", 1.0, 3.3, 98],
 ["Hallsberg", "2018-03-06", "mar", 3.7, 2.3, 142],
 ["Malmo", "2018-01-10", "jan", 1.0, 2.9, 112],
 ["Hallsberg", "2018-04-29", "apr", 2.7, 2.3, 100]])

df.columns = ['City', 'Date', 'Month', 'Mean1', 'Mean2', 'Mean3']

df["Val1"] = math.exp(-df["Mean1"])

print(df)