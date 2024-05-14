import numpy as np
from datetime import datetime
dt = datetime.utcnow()
print('Current date:')
print(dt)
dt64 = np.datetime64(dt)
print('Timestamp:')
print(ts)
print('UTC from Timestamp:')
print(datetime.utcfromtimestamp(ts))