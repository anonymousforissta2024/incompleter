#Source: https://stackoverflow.com/questions/67560562/pandas-read-csv-error-i-e-filenotfounderror-errno-2-no-such-file-or-direct
file_path = "%s.csv" % (i)
df = pd.read_csv(file_path)
sma_padded = np.concatenate([np.zeros(len(df) - sma.shape[0]), sma])
df['SMA'] = pd.Series(sma_padded, index=df.index)   
df.to_csv(file_path, index=False)