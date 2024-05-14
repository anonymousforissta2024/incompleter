#Source: https://stackoverflow.com/questions/42988348/typeerror-cannot-convert-the-series-to-class-float
df["B"] = math.log(df["A"] / df["A"].shift(1))