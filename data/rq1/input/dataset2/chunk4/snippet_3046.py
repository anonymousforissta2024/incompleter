#Source: https://stackoverflow.com/questions/64749731/cant-subtract-hours-from-time-data-because-of-data-type-error
df['Hours'] = df['Hours'].astype('datetime64')
df['Hours'] = pd.to_datetime(df['Hours']).dt.time
df['Hours'] = pd.to_datetime(df['Hours']).dt.floor('d')