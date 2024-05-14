#Source: https://stackoverflow.com/questions/59044361/typeerror-an-integer-is-required-got-type-datetime-datetime-when-trying-to-co
import datetime

dic = {'Select start date': datetime.datetime(2019, 11, 7, 0, 0)}

for key, value in dic.items():
     d = datetime.datetime(value)
     d.strftime("%d %b %Y")   