#Source: https://stackoverflow.com/questions/54917838/attributeerror-module-pandas-has-no-attribute-rolling-mean-temp-append
temp.append(pd.rolling_mean(pd.pivot_table(telemetry,
   index='datetime',
   columns='machineID',
   values=col), window=24).resample('3H',
        closed='left',
        label='right',
        how='first').unstack())