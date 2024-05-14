#Source: https://stackoverflow.com/questions/72884714/attributeerror-nonetype-object-has-no-attribute-languages
import ocrmypdf
import camelot
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

# if filename is not None:
if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
    ocrmypdf.ocr (filename, 'output.pdf', deskew=True,)

file = "output.pdf"
tables = camelot.read_pdf(file, pages = "1-end", flavor='stream')
print(tables.n)
tables=camelot.read_pdf(file, pages='1-end', flavor='stream')
tables.export(filename + ".xlsx", f='excel')