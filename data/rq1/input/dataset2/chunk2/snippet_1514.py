#Source: https://stackoverflow.com/questions/42123141/pandas-timestamp-conversion-type-error
import datatime as dt

print(type(row['my_timestamp']))
current_date = dt.date.fromtimestamp(row['my_timestamp'])