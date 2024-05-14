#Source: https://stackoverflow.com/questions/67757892/typeerror-cannot-convert-the-series-to-class-int-in-to-date
df['start_data'] = df['start_time'].astype(int)