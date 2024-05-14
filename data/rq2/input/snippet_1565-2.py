from datetime import date, timedelta
from random import choices
test_date1, test_date2 = (date(2015, 6, 3), date(2015, 7, 1))
print('The original range : ' + str(test_date1) + ' ' + str(test_date2))
K = 7
res_dates = [test_date1]
while test_date1 != test_date2:
    test_date1 += timedelta(days=1)
    res_dates.append(test_date1)
print('K random dates in range : ' + str(res))