from datetime import datetime
from dateutil.parser import parse
print('Convert datatime to strings:')
print(stamp.strftime('%Y-%m-%d'))
print(stamp.strftime('%d/%b/%y'))
print('\nConvert strings to datatime:')
print(parse('Sept 17th 2019'))
print(parse('1/11/2019'))
print(parse('1/11/2019', dayfirst=True))