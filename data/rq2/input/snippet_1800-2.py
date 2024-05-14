import calendar
year = 1997
print('The original year : ' + str(year))
res = []
for month in range(1, 13):
    res.append(str(max((week[weekdy] for week in calendar.monthcalendar(year, month)))) + '/' + str(month) + '/' + str(year))
print('Last weekdays of year : ' + str(res))