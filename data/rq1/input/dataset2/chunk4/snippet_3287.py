#Source: https://stackoverflow.com/questions/63678164/pandas-reset-index-gives-typeerror-cannot-compare-types-ndarraydtype-float64
# get all csv files, append to list
file_list = list()
for file in table_files:
    df_file = pd.read_csv(pdf_data_path + file, header=None)
    file_list.append(df_file)

# create new df from file list
df_raw = pd.concat(file_list, axis=0, ignore_index=True)

# remove trailing spaces entire df 
df_all = df_raw.applymap(lambda x: x.rstrip() if type(x)==str else x)

# exclude top 2 rows
df_all = df_all.iloc[2:]

# drop empty rows
df_all.dropna(how='all', inplace = True) 