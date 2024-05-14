#Source: https://stackoverflow.com/questions/72708057/typeerror-unsupported-operand-types-for-float-and-datetimearray
start_date = r'12/12/1984'
end_date = r'12/12/1986'

date1 = time.mktime(datetime.datetime.strptime(start_date, "%m/%d/%Y").timetuple())
date2 = time.mktime(datetime.datetime.strptime(end_date, "%m/%d/%Y").timetuple())

df = df[df['CreatedDate'] > date1 & df['CreatedDate'] <= date2 ]