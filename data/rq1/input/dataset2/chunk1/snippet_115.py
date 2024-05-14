#Source: https://stackoverflow.com/questions/55035784/typeerror-can-only-perform-ops-with-scalar-values
tables = pd.read_html('https://www.iasplus.com/en/resources/ifrs-topics/use-of-ifrs', header = None)

df = tables[2]

df.columns = df.columns.get_level_values(0)  + ":" + df.columns.get_level_values(1)

sns.countplot( "Domestic unlisted companies:Use of IFRSs by unlisted companies", data=df)