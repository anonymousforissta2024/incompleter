import pandas as pd
dtt = dtt.tz_localize('UTC')
print(dtt)
print('\nFrom UTC to America/Los_Angeles:')
dtt = dtt.tz_convert('America/Los_Angeles')
print(dtt)