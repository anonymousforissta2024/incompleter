#Source: https://stackoverflow.com/questions/64749731/cant-subtract-hours-from-time-data-because-of-data-type-error
if df[df["Hour"] < 0].all().all()  and df["Hours"].all().all() != -12.1:
    df["EndTime"] = pd.to_datetime(df["EndTime"]) - timedelta(hours=12) 