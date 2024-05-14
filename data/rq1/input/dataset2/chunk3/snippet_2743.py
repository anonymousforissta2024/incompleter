#Source: https://stackoverflow.com/questions/62668497/pypdf2-byte-data-vs-binary-data-typeerror
from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = "/file_path/.pdf"

input_pdf = PdfFileReader(file_path)
output_file = PdfFileWriter()

cover_page = input_pdf.getPage(0)
output_file.addPage(cover_page)

with open("portion.pdf", "wb") as output_file:
    output_file.write(output_file)