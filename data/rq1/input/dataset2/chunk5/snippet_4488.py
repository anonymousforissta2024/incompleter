#Source: https://stackoverflow.com/questions/59221078/typeerror-unhashable-type-numpy-ndarray-arima-time-series
Combined = pd.read_csv(file_path, parse_dates=['Revenue_mth'], index_col = ['Revenue_mth'])
plt.xlabel('Date')
plt.ylabel('Revenue amount')
plt.plot(Combined)