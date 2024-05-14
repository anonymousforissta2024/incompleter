#Source: https://stackoverflow.com/questions/7050894/nameerror-name-self-is-not-defined-when-passing-attribute-as-parameter-to-met
from pyPdf import PdfFileWriter, PdfFileReader
import re
import time

class PdfGet():
    def __init__(self):
        self.initialize()

    def initialize(self):
        while True:
            raw_args = input('Welcome to PdfGet...\n***Please Enter Arugments (infile,outfile,start_page,end_page) OR type "quit" to exit***\n').strip() 
            if raw_args.lower() == 'quit':
                break
            print("Converting Pdf...")
            self.args = re.split(r',| ',raw_args)
            self.opener(*self.args[0:1])
            if len(self.args)== 4:
                self.pageoutput(*self.args[1:])
            elif len(self.args) == 3:
                self.pageoutput(*self.args[1:3])
            else:
                self.pageoutput(*self.args[1:2])
            print("Successfuly Converted!")
            nextiter = input('Convert Another PDF? (Type "yes" or "no")').lower()
            if nextiter == 'no':
                break

    def opener(self,infile):
        self.output = PdfFileWriter()
        self.pdf = PdfFileReader(open(infile, "rb"))
        self.pagenum = self.pdf.getNumPages()
        self.lastpage = self.pagenum+1
        print(self.lastpage)

    def pageoutput(self,outfile,start_page=0,end_page=self.lastpage):
        for i in range (int(start_page)-1,int(end_page)):
            self.output.addPage(self.pdf.getPage(i))    
        outputStream = open(outfile, "wb")
        self.output.write(outputStream)
        outputStream.close()

if __name__ == "__main__":
    PdfGet()
    time.sleep(5)