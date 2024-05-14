#Source: https://stackoverflow.com/questions/74396402/python-pandas-attributeerror-dict-object-has-no-attribute-head
df = pd.read_excel(download_path, sheet_name=None)
l = df.values.tolist()