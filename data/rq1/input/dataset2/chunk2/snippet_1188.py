#Source: https://stackoverflow.com/questions/75353814/python-google-or-tools-surgical-booking-attributeerror-dataframe
# Input data from excel sheet columns

dfP = pd.DataFrame(data, columns=["Procedure"])
dfP = dfP.iloc[:, :].values.tolist()
dfP = [x for y in dfP for x in y]

dfD = pd.DataFrame(data, columns=["Date"])
dfD = dfD.iloc[:, :].values.tolist()
dfD = [x for y in dfD for x in y]

dfE = pd.DataFrame(data, columns=["Book Dur"])
dfE = dfE.iloc[:, :].values.tolist()
dfE = [x for y in dfE for x in y]

dfA = pd.DataFrame(data, columns=["Actual Dur"])
dfA = dfA.iloc[:, :].values.tolist()
dfA =  [x for y in dfA for x in y]