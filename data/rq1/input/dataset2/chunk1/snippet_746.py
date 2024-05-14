#Source: https://stackoverflow.com/questions/54461293/trying-to-convert-object-to-datetime-getting-typeerror
df['Time'] = df['Time'].apply(pd.Timestamp)