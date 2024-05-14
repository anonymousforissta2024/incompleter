#Source: https://stackoverflow.com/questions/44999650/error-nameerror-name-values-is-not-defined
def summary_stats(col_name, col_data):
    values = {'column name' : col_name,
    'mean' : np.mean(col_data),
    'median' : np.median(col_data),
    'variance' : np.var(col_data),
    'standard deviation' : np.std(col_data)}

for key, value in values.items():
    print(key, ':' , value)