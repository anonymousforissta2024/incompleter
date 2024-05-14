#Source: https://stackoverflow.com/questions/73115690/converting-list-requested-from-api-to-dataframe-attributeerror-list-object-ha
from datetime import datetime
dates=[ '01-01-2021','01-04-2021','01-07-2021','01-10-2021',
        '01-01-2022','01-04-2022','01-07-2022']

# Convert your strings to datetime, using `datetime` library
dates = [datetime.strptime(date, "%d-%m-%Y") for date in dates]



def create_df(pair,dates):
    df = []
    for index, elem in enumerate(dates):
        if index== 0:
            curr_date = str(elem.timestamp())
            next_date = str(dates[index+1].timestamp())
            df = client.get_prices_intraday(pair, interval = '1m', from_ = curr_date, to = next_date)
        elif ((index>0) & (index+1 < len(dates))):
            curr_date = str(elem.timestamp())
            next_date = str(dates[index+1].timestamp())
            df2 = client.get_prices_intraday(pair, interval = '1m', from_ = curr_date, to = next_date)
            df.append(df2)
    return df






from eod import EodHistoricalData
# create the instance of the SDK
api_key = 'my_api_key'
client = EodHistoricalData(api_key)




GBPAUD = create_df('GBPAUD.FOREX',dates)