#Source: https://stackoverflow.com/questions/57563202/pandas-typeerror-textfilereader-object-is-not-subscriptable
e1 = pd.read_csv(working_dir+"E1.txt",sep=',', chunksize = 10000)
e1['MTM'] = e1['stack_over_flow']