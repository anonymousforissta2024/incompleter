from datetime import datetime
isoformat_date = todays_Date.isoformat()
print(type(isoformat_date))
result = datetime.fromisoformat(isoformat_date)
print(type(result))