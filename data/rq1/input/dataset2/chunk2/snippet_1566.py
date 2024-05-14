#Source: https://stackoverflow.com/questions/69001132/use-zip-to-combine-list-with-dataframe-attributeerror-str-object-has-no-att
final_dataset_list = []
for date, df in zip(date_list, df_dataset):
    if len(df) == 0:
        continue
    df.loc[:, 'date'] = pd.to_datetime(date)
    final_dataset_list.append(df)