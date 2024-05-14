#Source: https://stackoverflow.com/questions/67229203/typeerror-data-type-list-not-understood
a = {'Id': {0: 1, 1: 2, 2: 3},
 'col': {0: 5.1, 1: 4.9, 2: 4.9}}
d = pd.DataFrame.from_dict(a)
attr_unique_val = d.groupby('col')['Id'].unique()
attr_unique_val = attr_unique_val.astype('list')