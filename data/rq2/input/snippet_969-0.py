import pandas as pd
time_stamp = pd.to_datetime(epoch_t, unit='s')
print('Regular time stamp in UTC:')
print(time_stamp)
print('\nConvert the said timestamp in to US/Pacific:')
print(time_stamp.tz_localize('UTC').tz_convert('US/Pacific'))
print('\nConvert the said timestamp in to Europe/Berlin:')
print(time_stamp.tz_localize('UTC').tz_convert('Europe/Berlin'))