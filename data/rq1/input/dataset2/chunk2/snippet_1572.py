#Source: https://stackoverflow.com/questions/51110837/dataframe-attributeerror-nonetype-object-has-no-attribute-iloc
for j in range(column): #Column is the number of columns in the dataframe 'traindata'
    if np.all(traindata.iloc[:, j] == 0): #Compare all values in a column to 0 
        traindata = traindata.drop(traindata.columns[j], axis=1, inplace=True)                
print(traindata.shape)