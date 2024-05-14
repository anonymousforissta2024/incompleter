#Source: https://stackoverflow.com/questions/62163197/typeerror-passing-series-with-dtype-int-to-dateutil-relativedelta
df.loc[:,'calc_eli_date'] = (
    datetime.datetime(df['pol_eff_date'])
    + relativedelta(years=df['frt_elig_year'])
)