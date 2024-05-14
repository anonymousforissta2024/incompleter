#Source: https://stackoverflow.com/questions/62858221/typeerror-pdffilewriter-object-is-not-callable
from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_file_path = "oranges.pdf"
file_base_name = pdf_file_path.replace(".pdf","")

pdf = PdfFileReader(pdf_file_path) #Creating PDF instance
pages = [0,2,4]

pdfwriter = PdfFileWriter() #Creating pdfWriter instance
print

for page_num in pages:
    pdfwriter().addPage(pdf.getPage(page_num))
with open("{0}_subset".format(file_base_name),'wb') as f:
    pdfwriter.write(f)
    f.close