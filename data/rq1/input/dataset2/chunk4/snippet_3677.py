#Source: https://stackoverflow.com/questions/59225923/attribute-error-white-extracting-column-from-a-csv-file
import pandas as pd
from astropy.table import Table

#reading the data from the dataset file
data=pd.read_csv('winequality-red.csv',sep=',')

#Declaring a class named as One
class One: 
    def __init__(self):
        # Assigning the value that are less than 11 in
        # the data set to the value data_lessthan11
        data_lessthan11 = data.loc[(data.quality<11)]

        # Assigning the filtered value from the data_less
        # than11(which consists of values less than 11)
        # which is greater than 5
        self.data_greaterthan5 = data.loc[(data_lessthan11.quality>5)]
        print(data_lessthan11)

#declaring an object for the class One
one = One()

# assigning the whole value from the class one into
# size_One to recall it outside the class
size_One = one.data_greaterthan5

print(size_One)