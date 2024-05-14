#Source: https://stackoverflow.com/questions/58168488/type-hint-returns-nameerror-name-datetime-not-defined
def time_in_range(start: datetime, end: datetime, x: datetime) -> bool:
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end