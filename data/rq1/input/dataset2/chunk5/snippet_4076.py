#Source: https://stackoverflow.com/questions/61775499/pivot-table-function-not-working-attributeerror-numpy-ndarray-object-has-no
no_row_df = pd.pivot_table(no_row_data, values = "FINALWT", index = ["SURVDATE", "PROV"], aggfunc=np.sum)
for col in count_columns:
    table = pd.pivot_table(no_row_data, values = "FINALWT", index = ["SURVDATE", "PROV"], columns=[col], aggfunc=np.sum)
    no_row_df = df.merge(table, left_index=True, right_on=["SURVDATE", "PROV"])
no_row_df