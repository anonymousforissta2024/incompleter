#Source: https://stackoverflow.com/questions/65372742/python-kivy-attributeerror-nonetype-object-has-no-attribute-text
#exel database
import xlrd, xlwt
from xlutils.copy import copy
import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.loadinfo = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.loadinfo = {}

        for line in self.file:
            invoice, purpose, carrier, cost, local, outcal, Driver, Dispatcher = line.strip().split(";")
            self.loadinfo[invoice] = (invoice, purpose, carrier, cost, local, outcal, Driver, Dispatcher)

        self.file.close()

    def top_right(self, invoice, purpose):
        pass

    def add_loadinfo(self, invoice, purpose, carrier, cost, local, outcal, Driver, Dispatcher):
        self.loadinfo[invoice.strip()] = (invoice.strip(), purpose.strip(), carrier.strip(), cost.strip(), local.strip(), outcal.strip(), Driver.strip(), Dispatcher.strip(), DataBase.get_date())
        self.save()

    
    def save(self):
        with open(self.filename, "w") as f:
            for loadinfo in self.loadinfo:
                f.write(loadinfo + ";" + self.loadinfo[invoice][0] + ";" + self.loadinfo[invoice][1] + ";" + self.loadinfo[invoice][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
        

#code to put it into excel

# read_book = xlrd.open_workbook("Invoice.xls", formatting_info=True) #Make Readable Copy
# write_book = copy(read_book) #Make Writeable Copy

# write_sheet1 = write_book.get_sheet(1) #Get sheet 1 in writeable copy
# write_sheet1.write(1, 11, self.invoice.text) #Write 'test' to cell (1, 11)

# write_sheet2 = write_book.get_sheet(2) #Get sheet 2 in writeable copy
# write_sheet2.write(3, 14, '135') #Write '135' to cell (3, 14)

# write_book.save("New/File/Path") #Save the newly written copy. Enter the same as the old path to write over