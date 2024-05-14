#Source: https://stackoverflow.com/questions/76226271/i-am-getting-attribute-error-for-append-in-pandas-even-for-concat
df = pd.DataFrame(df).append(new_row, ignore_index=True)