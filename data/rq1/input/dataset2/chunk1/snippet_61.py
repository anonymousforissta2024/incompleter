#Source: https://stackoverflow.com/questions/46995307/attributeerror-in-python-static-method
import datetime as dt
from helpers import str2date

from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday, \
    USMartinLutherKingJr, USPresidentsDay, GoodFriday, USMemorialDay, \
    USLaborDay, USThanksgivingDay


class USTradingCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('NewYearsDay', month=1, day=1, observance=nearest_workday),
        USMartinLutherKingJr,
        USPresidentsDay,
        GoodFriday,
        USMemorialDay,
        Holiday('USIndependenceDay', month=7, day=4, observance=nearest_workday),
        USLaborDay,
        USThanksgivingDay,
        Holiday('Christmas', month=12, day=25, observance=nearest_workday)
    ]


    @classmethod
    def get_trading_close_holidays(cls, year):
        return cls.holidays(dt.datetime(year-1, 12, 31), dt.datetime(year, 12, 31))



if __name__ == '__main__':
    print(USTradingCalendar.get_trading_close_holidays(2016))