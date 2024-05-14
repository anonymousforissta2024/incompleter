import datetime
print('Original time:')
print(date_and_time)
time_change = datetime.timedelta(minutes=75)
new_time = date_and_time + time_change
print('changed time:')
print(new_time)