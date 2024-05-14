#Source: https://stackoverflow.com/questions/62732790/apply-a-function-to-columns-in-pandas-raises-attributeerror
sample_dict = {'isDuplicate': {'1051681551': False, '1037545402': True, '1035390559': False},
               'dateTime': {'1051681551': Timestamp('2019-01-29 09:09:00+0000', tz='UTC'),
               '1037545402': Timestamp('2019-01-11 02:06:00+0000', tz='UTC'),
               '1035390559': Timestamp('2019-01-08 14:35:00+0000', tz='UTC')},
               'dateTimePub': {'1051681551': None, '1037545402': None, '1035390559': None}}

df = pd.DataFrame.from_dict(sample_dict)