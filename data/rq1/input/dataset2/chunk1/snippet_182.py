#Source: https://stackoverflow.com/questions/47939513/name-error-when-calling-defined-function-in-jupyter
def merge_dfs_on_column(dataframes, labels, col):
    '''merge a single column of each dataframe on to a new combined dataframe'''
    series_dict={}
    for index in range(len(dataframes)):
        series_dict[labels[index]]=dataframes[index][col]
    return pd.DataFrame(series_dict)
# Merge the BTC price dataseries into a single dataframe
btc_usd_datasets= merge_dfs_on_column(list(exchange_data.values()),list(exchange_data.keys()),'Weighted Price')