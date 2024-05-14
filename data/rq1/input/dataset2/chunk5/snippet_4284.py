#Source: https://stackoverflow.com/questions/62364735/how-to-fix-typeerror-data-type-not-understood-with-a-datetime-object-in-pandas
user_groups = df1.groupby("customer_id")["month"]

df1["Cohort_month"] = user_groups.transform("min")