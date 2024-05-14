#Source: https://stackoverflow.com/questions/21100117/encountering-typeerror-with-csv-writer
import os
import csv
import tempfile

def importFromCSV(filepath):
    print("Reading data from",os.path.basename(filepath))
    datalist = []
    with open(filepath) as csvfile:
        file_dialect = csv.Sniffer().sniff(csvfile.readline(),[',',';',':','\t','.'])
        csvfile.seek(0)
        filereader = csv.reader(csvfile,dialect = file_dialect)
        for row in filereader:
            datalist.append(row)
    return datalist

def SplitToTemp(datalist, target_dir):
    tmpnamelist = []
    templist = []
    for item in datalist:
        if item[0] != '':
            templist.append(item)
        else:
            del item
            f = tempfile.NamedTemporaryFile(delete = False, dir = target_dir)
            tmpnamelist.append(f.name)
            dw = csv.writer(f, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
            for row in templist:
                dw.writerow(row)
            f.close()
            templist = []
    return tmpnamelist

###############################################################################
pathname = os.path.normpath('C:/Python33/myprograms/myclassandfx/BenchLink/blrtest.csv')
tempdir = tempfile.mkdtemp(dir = os.path.normpath('c:/users/'+os.getlogin()+'/desktop'))

filedata = import_from_csv(pathname)
tempnames = SplitToTemp(filedata, tempdir)