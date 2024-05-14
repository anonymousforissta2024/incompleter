import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('Original DataFrame:')
print(df)
dict_data_list = list()
for gg, dd in df.groupby(['school_code', 'class']):
    group = dict(zip(['school_code', 'class'], gg))
    ocolumns_list = list()
    for _, data in dd.iterrows():
        data = data.drop(labels=['school_code', 'class'])
        ocolumns_list.append(data.to_dict())
    group['other_columns'] = ocolumns_list
    dict_data_list.append(group)
print(dict_data_list)