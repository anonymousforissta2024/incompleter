import pandas as pd
q_start_dates = pd.date_range('2020-01-01', '2020-12-31', freq='BQS-JUN')
print('All the business quarterly begin dates of 2020:')
print(q_start_dates.values)
print('\nAll the business quarterly end dates of 2020:')
print(q_end_dates.values)