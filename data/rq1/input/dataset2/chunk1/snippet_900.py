#Source: https://stackoverflow.com/questions/57291797/dask-attributeerror-dataframe-object-has-no-attribute-getitem-array
train_churn = train[train['CON_CHURN_DECLARATION'] == 1]
train_churn.compute()