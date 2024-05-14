#Source: https://stackoverflow.com/questions/58672758/typeerror-data-type-not-understood-while-parsing-csv-with-pandas
import pandas as pd
import datetime as datetime

data = pd.read_csv("scans.csv")

# dtypes = {
#     'date': datetime,
#     'muscle': str,
#     'side': str,
#     'MQ(0-100)': float,
#     'MQ(raw)': int,
#     'fat': float
# }
# data = pd.read_csv("scans.csv", dtype=dtypes)

print(data.head())
print(data.dtypes)