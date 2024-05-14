#Source: https://stackoverflow.com/questions/73471240/typeerror-unsupported-operand-types-for-str-and-datetime-timedelta
def date_return():
    return date


date_return() + datetime.timedelta(days=10) 