#Source: https://stackoverflow.com/questions/55476347/how-to-eliminate-type-error-while-using-pandas-apply-function-with-a-lambda-expr
#import modules
import pandas as pd

#define functions
def read_datafile():
    d = pd.read_csv('cmc.data.txt', sep=',')
    return d

def create_bin_label(data):
    data['numchildren'] = data.apply(lambda row: 1 if (row['number of children']) <= 0 else 0, axis=1)
    data = data.drop(['number of children'], axis=1)

#read in datafile
data = read_datafile()
print(len(data))

#create a binary label column and delete the old column
bl = create_bin_label(data)
print(data.head())