#Source: https://stackoverflow.com/questions/53047366/typeerror-when-calling-resample-in-pandas
import pandas_datareader.data as web
from datetime import datetime
# removed imports related to plotting

TRAIN_SIZE = 0.2
FORECAST_STEPS = 20
STOCKS_PREDICT = ['SPY', 'AAPL']


def downloadData(startDate, endDate):

    histPanel = web.DataReader(STOCKS_PREDICT, 'iex' , startDate, endDate)
    contains_condition = ((histPanel.isnull()) | (histPanel == 0)).any(axis=1)
    to_keep = contains_condition[contains_condition == False].index
    histPanel = histPanel.loc[to_keep]

    return histPanel


print(downloadData("01/01/2017","01/01/2019"))


def doForecast(Panel):

    closeDF = Panel['close']
    ts = closeDF['SPY']
    tsWeekly = ts.resample('W-MON').last() # TypeError here
    values = tsWeekly.tolist()
    
    # removed unrelevant plotting code


def main():
    startDate = datetime(2017, 1, 1)
    endDate = datetime.today()

    panel = downloadData(startDate, endDate)

    doForecast(panel)


if __name__ == '__main__':
    main()