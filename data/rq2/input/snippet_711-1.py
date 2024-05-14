import numpy as np
import datetime
dt_array = np.array([start + datetime.timedelta(hours=i) for i in range(24)])
print(dt_array)