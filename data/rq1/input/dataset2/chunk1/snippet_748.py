#Source: https://stackoverflow.com/questions/67447825/while-using-automl-from-evalml-getting-error-attributeerror-datatable-object
df.loc[(df.quality<6), 'flag_class'] = 1
df.loc[(df.quality==6), 'flag_class'] = 2
df.loc[(df.quality>6), 'flag_class'] = 3