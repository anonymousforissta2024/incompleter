#Source: https://stackoverflow.com/questions/17270387/pypdf2-typeerror-when-trying-to-extract-text
filename = "myfile.pdf"
f = open(filename,'rb')
mypdf = PdfFileReader(f)
print(f,mypdf,mypdf.getNumPages())
print(mypdf.getPage(0).extractText())