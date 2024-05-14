#Source: https://stackoverflow.com/questions/63237885/pandas-pd-to-datetime-returns-typeerror-class-type-is-not-convertible-to-da
filemeta_df[["filecreatedatetime_utc"]] = filemeta_df[["filecreatedatetime_utc"]].apply(pd.to_datetime(arg=int,utc=True))
filemeta_df[["fileupdatedatetime_utc"]] = filemeta_df[["fileupdatedatetime_utc"]].apply(pd.to_datetime(arg=int,utc=True))