import pandas as pd
import datetime
from datetime import datetime, date
sdt = datetime(2020, 1, 1)
dateset = pd.period_range(sdt, edt, freq='M')
print('All monthly boundaries of a given year:')
print(dateset)
print('\nStart and end time for each period object in the said index:')
for d in dateset:
    print('{0} {1}'.format(d.start_time, d.end_time))