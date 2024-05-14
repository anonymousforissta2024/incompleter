import numpy as np
from datetime import datetime
dt = datetime.utcnow()
print('Current date:')
print(dt)
ts = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
print('Timestamp:')
print(ts)
print('UTC from Timestamp:')
print(datetime.utcfromtimestamp(ts))