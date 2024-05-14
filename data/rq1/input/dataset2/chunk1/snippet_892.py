#Source: https://stackoverflow.com/questions/40582073/trying-to-iterate-and-join-pandas-dfs-attributeerror-series-object-has-no-at
'''
Import the modules necessary for analysis
'''

import quandl
import pandas as pd
import numpy as np

'''
Set file pathes and API keys
'''

ticker_path = ''
auth_key = ''

'''
Pull a list of tickers in the IGM ETF
'''

def ticker_list():
    df = pd.read_csv('{}IGM Tickers.csv'.format(ticker_path))
    # print(df['Ticker'])
    return df['Ticker']

'''
Pull the historical prices for the securities within Ticker List
'''

def grab_constituent_data():
    tickers = ticker_list()
    main_df = pd.DataFrame()

    for abbv in tickers:
        query = 'EOD/{}'.format(str(abbv))
        df = quandl.get(query, authtoken=auth_key)
        print('Competed the query for {}'.format(query))

        df['{} Adj_Close'.format(str(abbv))] = df['Adj_Close'].copy()
        df = df['{} Adj_Close'.format(str(abbv))]
        print('Completed the column adjustment for {}'.format(str(abbv)))

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print(main_df.head())