#Source: https://stackoverflow.com/questions/56574188/python-3-how-to-fix-filenotfounderror-errno-2-no-such-file-or-directory
##Working Code:
class backtest:

    def __init__(self, ticker):

        start = '1/3/2000'
        end = '1/3/2019'
        sdate = pd.to_datetime(start)
        edate = pd.to_datetime(end)


        if os.path.islink('{}_{}_to_{}.csv'.format(ticker, start, end)) == True:
            self.df = pd.read_csv('{}_{}_to_{}.csv'.format(ticker, start, end), parse_dates=True)

        else:
            ##Failed attempt 1
            ##self.filename = '{}_{}_to_{}.csv'.format(ticker, start, end)
            ##self.df.to_csv(self.filename)

            ##Failed attempt 2
            ##self.filename = str(ticker) + '_' + start + '_to_' + end + '.csv'            
            ##self.df.to_csv(self.filename)

            self.df = web.DataReader(ticker, 'yahoo', sdate, edate)
            self.df.to_csv('amzn_1/3/2000_to_1/3/19.csv')



amzn = backtest('amzn')
print(amzn.df.head(1))