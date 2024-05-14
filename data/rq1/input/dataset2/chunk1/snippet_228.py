#Source: https://stackoverflow.com/questions/54629368/pandas-attributeerror-dataframe-object-has-no-attribute-dt-when-using-apply
df_code_grp_by = df.groupby(['code'])

df_code_grp_by.apply(lambda x: x.date2 - x.date1).dt.days.sum(level=0).reset_index(name='date_diff_sum')