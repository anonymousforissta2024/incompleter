#Source: https://stackoverflow.com/questions/54635859/csv-writerow-raising-an-attributeerror
import csv

class File:
    def __init__(self, f):
        self.f = f

    def __add__(self, other):
        with open(self.f, mode='a') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"')
            f.writerow(str(other))
            return self.__str__()

o = File('file.csv')
s = o + 2