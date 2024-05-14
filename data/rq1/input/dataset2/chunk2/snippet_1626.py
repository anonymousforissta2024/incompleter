#Source: https://stackoverflow.com/questions/47613582/convert-epoch-to-datetime-format-python-typeerror
df['Time'] = pd.to_numeric(df['Time'], errors='coerce').fillna(0)
df['Time'].dtype