import datetime
from datetime import datetime
datetime_obj = datetime.strptime(datetime_str, '%d%b%Y%H%M%S')
print(datetime_obj)
time = datetime_obj.time()
print(time)