#Source: https://stackoverflow.com/questions/60698871/python-error-typeerror-class-pandas-libs-tslibs-timedeltas-timedelta-is
df['ActualOutage'] = df.apply(calc_value,axis=1) 