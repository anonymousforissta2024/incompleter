#Source: https://stackoverflow.com/questions/72771120/pymupdf-attributeerror-document-object-has-no-attribute-loadpage
import fitz
# read pdf file
pdf = fitz.open(file_path_name)
# load pdf page using index
page = pdf.loadPage(0)