#Source: https://stackoverflow.com/questions/45981145/inheriting-from-a-class-datetime-date-causes-a-super-init-too-many
FORMAT__DD_MM_YYYY = "dd.mm.yyyy"
from datetime import date


class DateExtended(date):
    date_string = None
    date_format = None

    def __init__(self, year: int, month: int, day: int, date_format: str=None):
        super().__init__(year=year, month=month, day=day)
        self.date_format = date_format
        self.date_string = "{:02d}.{:02d}.{:04d}".format(self.day, self.month, self.year)

bla1 = DateExtended(year=2010, month=5, day=3, date_format=FORMAT__DD_MM_YYYY_DOT)