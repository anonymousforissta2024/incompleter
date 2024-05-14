#Source: https://stackoverflow.com/questions/44596421/subtracting-1-column-of-a-datetimeindex-from-another-throws-valueerrors-and-type
dosage = test_df[test_df > 0][[7,8]].dropna()