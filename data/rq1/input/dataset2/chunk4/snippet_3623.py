#Source: https://stackoverflow.com/questions/75664440/attributeerror-nonetype-object-has-no-attribute-get-object
pdf_reader = pypdf.PdfReader(file_path, strict=False)
print(pdf_reader.trailer['/Root']['/Pages']) 