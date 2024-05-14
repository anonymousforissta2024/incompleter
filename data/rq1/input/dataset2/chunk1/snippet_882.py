#Source: https://stackoverflow.com/questions/54991008/attributeerror-series-object-has-no-attribute-iterrows
accounts = pd.read_csv('C:/*******/New_export.txt', sep=",", dtype={'number': object})
accounts.columns = ["Number", "F"]

for i, j in accounts["Number"].iterrows(): #i represents the row(index number), j is the number
    if (str(j) == "27*******5"):
        print(accounts["F"][i], accounts["Number"][i])