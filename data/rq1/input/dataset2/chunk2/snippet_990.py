#Source: https://stackoverflow.com/questions/59863756/python-typeerror-when-generating-a-list-of-dates
from pandas.tseries import offsets

years = []
for i in  range(1990,2020):
    offsets.YearBegin(years).append(i)