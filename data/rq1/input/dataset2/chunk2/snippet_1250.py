#Source: https://stackoverflow.com/questions/69088617/typeerror-can-not-infer-schema-for-type-class-datetime-timedelta
df_dif=df_lag_drp.rdd.map(lambda x: (x["prev_row_startdate"]-x["FINISH_DATE"]))