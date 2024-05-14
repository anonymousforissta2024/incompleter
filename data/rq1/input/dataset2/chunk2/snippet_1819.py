#Source: https://stackoverflow.com/questions/47613582/convert-epoch-to-datetime-format-python-typeerror
df['Time'] = time.strftime("%d-%m", time.localtime(df['Time']))