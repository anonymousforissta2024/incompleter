import calendar
print('The original year : ' + str(year))
weekdy = 5
res = []
for month in range(1, 13):
    res.append(str(max((week[weekdy] for week in calendar.monthcalendar(year, month)))) + '/' + str(month) + '/' + str(year))
print('Last weekdays of year : ' + str(res))