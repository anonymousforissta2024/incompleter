#Source: https://stackoverflow.com/questions/53671612/apriori-model-has-typeerror-unorderable-types-float-str
dataset = pd.read_csv("Market_Basket_Optimisation.csv", header = None)
transactions =[]
for i in range(0,7501):
      transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

#training of dataset
from apyori import apriori
rules = apriori(transactions,min_support=0.003,min_confidence=0.2,min_lift=3,min_lenght=2)
res= list(rules)