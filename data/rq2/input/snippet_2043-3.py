import datetime
test_date1 = datetime.datetime(1997, 1, 4)
test_date2 = datetime.datetime(1997, 1, 30)
print('The original date 1 is : ' + str(test_date1))
print('The original date 2 is : ' + str(test_date2))
N = 7
temp = []
for idx in range(0, N):
    temp.append(test_date1 + idx * diff)
res = []
for sub in temp:
    res.append(sub.strftime('%Y/%m/%d %H:%M:%S'))
print('N equal duration dates : ' + str(res))