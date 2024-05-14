#Source: https://stackoverflow.com/questions/67333170/python-nameerror-after-introduction-of-if-clause
process_time_dfs = []
status_dfs = []

for string in filestrings:
    
    #read in command with apropriate delimiter and engine starting from a nmc-specific line in the excel doc
    EIS_TS_csv = pd.read_csv(DATA_DIR.joinpath(string), engine = 'python', delimiter = ';', skiprows = startposition)

    #drop [descriptor] row
    EIS_TS_csv.drop(index = 0, axis = 0, inplace = True)

    #add to dataframe
    status_dfs.append(EIS_TS_csv['Status'])
    process_time_dfs.append(EIS_TS_csv['Progr. Zeit'].str.replace('.', '').astype(float))