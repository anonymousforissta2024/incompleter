#Source: https://stackoverflow.com/questions/58340342/pandas-groupby-typeerror-not-supported-between-instances-of-seriesgroupby
group = df.groupby(['Id',  'Name'])
conditions = [
    ((group["Balance"]>0) & (group['Value']>0) & (group['L_Date']<=group['c_date'])),
    ((group["Balance"]==0) & (group['Value']==0) & (group['L_Date']<=group['c_date']))]
choices = ['Good', 'Bad']
df['outcome'] = np.select(conditions, choices, default='Normal')