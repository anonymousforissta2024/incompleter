#Source: https://stackoverflow.com/questions/71011031/attributeerror-dataframe-object-has-no-attribute-operation
def statSummary(dataset,operation):
    operation = []
    operation.append(df[dataset].operation())

    return print(operation)

#load dataset 
df = pd.read_csv('dataset.csv')

columnNames = list(df.columns)

ops = ["mean","median","std","max","min"]

for i in ops:
    statSummary(columnNames,i)