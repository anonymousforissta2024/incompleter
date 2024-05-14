import datetime
print('string datetime: ')
print(date_string)
print('datestring class is :', type(date_string))
datetime_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f %z')
print('converted to datetime:')
print(datetime_obj)
print('datetime_obj class is :', type(datetime_obj))