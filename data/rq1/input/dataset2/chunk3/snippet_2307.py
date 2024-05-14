#Source: https://stackoverflow.com/questions/48939168/python-error-typeerror-expected-string-or-buffer
half_hour_date = '23/02/2018 23:00PM'
epg_time_1 = time.strptime(half_hour_date, '%d/%m/%Y %I:%M%p')

#convert from time_struct_time object to datetime
date_format = datetime.datetime.fromtimestamp(time.mktime(epg_time_1))
half_hour = date_format + datetime.timedelta(days = self.program_day)

#convert from datetime to time_struct_time object
epg_time_1 = time.strptime(half_hour, '%d/%m/%Y %I:%M%p')