#Source: https://stackoverflow.com/questions/63678164/pandas-reset-index-gives-typeerror-cannot-compare-types-ndarraydtype-float64
split_index = (df_all[df_all.iloc[:,0]=='Platform'].index.item())