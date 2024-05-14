import pandas as pd
epoch_t = 1621132355
print('Regular time stamp in UTC:')
print(time_stamp)
print('\nConvert the said timestamp in to US/Pacific:')
print(time_stamp.tz_localize('UTC').tz_convert('US/Pacific'))
print('\nConvert the said timestamp in to Europe/Berlin:')
print(time_stamp.tz_localize('UTC').tz_convert('Europe/Berlin'))