#Source: https://stackoverflow.com/questions/58132205/attributeerror-type-object-datetime-datetime-has-no-attribute-timedelta
from datetime import datetime, time, timedelta

att1 = datetime.strptime('09:00 AM','%H:%M %p')

att2 = datetime.timedelta(minutes = 15)

time_zero = datetime.strptime('00:00 AM','%H:%M %p')

att3 =  (att1 - time_zero + att2).strftime("%X %p")

print(" sTime and Approx time is",att3)