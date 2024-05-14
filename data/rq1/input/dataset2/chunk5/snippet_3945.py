#Source: https://stackoverflow.com/questions/61387068/got-attribute-error-after-executing-the-knn-imputation
sales = pd.DataFrame(KNN(k = 3).complete(sales), columns = sales.columns)