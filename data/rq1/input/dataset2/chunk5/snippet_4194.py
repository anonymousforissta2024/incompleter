#Source: https://stackoverflow.com/questions/62364735/how-to-fix-typeerror-data-type-not-understood-with-a-datetime-object-in-pandas
df1["month"] = pd.to_datetime(Table_A_df['date']).dt.to_period('M')