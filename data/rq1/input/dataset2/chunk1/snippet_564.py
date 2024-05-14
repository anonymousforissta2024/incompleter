#Source: https://stackoverflow.com/questions/54013527/typeerror-unsupported-operand-types-for-slice-and-int-with-bt-backtest
#Format price data
csv_f = pd.read_csv('cryptodata.csv')
data = pd.DataFrame(csv_f)
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace = True)
df1 = data[:-1]
df1 = df1.dropna()

def momentum_strategy(data, mom1 = 15, mom2 = 30, mom3 = 60, selection = 5 , cost = 0.025):

    #Momentum calc 
    mom_1 = data.pct_change(mom1)
    mom_2 = data.pct_change(mom2)
    mom_3 = data.pct_change(mom3)

    mom_average = (mom_1 + mom_2 + mom_3) / 3
    mom_average = mom_average.dropna()

    #Weight
    mom_average_rank = mom_average.rank(1, ascending = True)
    mom_selection = selection > mom_average_rank

    #create strategy

    s = bt.Strategy('mom_s',[bt.algos.SelectWhere(mom_selection),
                        bt.algos.RunWeekly(),
                        bt.algos.SelectAll(),
                        bt.algos.WeighEqually(),
                        bt.algos.Rebalance()])

    return bt.Backtest(s, data, commissions = lambda q, p: max(100, abs(q) * cost ))

#create the backtests
mom_1 = momentum_strategy(df1, 15, 30, 60, 5, 0.025)

#run backtests
res = bt.run(mom_1)