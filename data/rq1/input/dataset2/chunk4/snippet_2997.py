#Source: https://stackoverflow.com/questions/73448351/datetime-typeerror-strptime-argument-1-must-be-str-not-timestamp
import datetime
import pandas as pd
dataset = pd.read_excel("D:\\DataSciencePython/retail_raw_reduced.xltx")
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
print(dataset.head())