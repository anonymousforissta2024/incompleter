#Source: https://stackoverflow.com/questions/52312736/getting-attributeerror-while-loading-and-accessing-the-data-using-csv-reader
import csv
import numpy
def loadCsv(filename):
    lines = csv.reader(open(filename,"r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset
filename = 'data1.csv'
dataset = loadCsv(filename)
print('Loaded data file {0} with {1} rows').format(filename, len(dataset))