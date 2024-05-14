#Source: https://stackoverflow.com/questions/60715059/python-backtrader-error-filenotfounderror-errno-2-no-such-file-or-directory
from datetime import datetime
import backtrader as bt

class SmaSignal(bt.Signal):
    param = (('period', 20), )

    def __init__(self):
        self.lines.signal = self.data - bt.ind.SMA(period=self.p.period)

data = bt.feeds.YahooFinanceData(dataname='AAPL',
                                fromdate=datetime(2018, 1, 1),
                                todate=datetime(2018, 12, 31))
cerebro = bt.Cerebro(stdstats=False)
cerebro.adddata(data)
cerebro.broker.setcash(1000.0)
cerebro.add_signal(bt.SIGNAL_LONG, SmaSignal)
cerebro.addobserver(bt.observers.BuySell)
cerebro.addobserver(bt.observers.Value)

print(f'Starting Portfolio Value: {cerebro.broker.getvalue():.2f}')
cerebro.run()
print(f'Final Portfolio Value: {cerebro.broker.getvalue():.2f}')
cerebro.plot(iplot=True, volume=False)