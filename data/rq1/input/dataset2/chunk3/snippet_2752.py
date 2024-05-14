#Source: https://stackoverflow.com/questions/60698871/python-error-typeerror-class-pandas-libs-tslibs-timedeltas-timedelta-is
df['ActualLength'] =  calc_timeDiff(df['Actual Int Start Time'],df['Actual Int End Time'])
df['NotifiedLength'] =  calc_timeDiff(df['Notified Start Time'],df['Notified End Time'])