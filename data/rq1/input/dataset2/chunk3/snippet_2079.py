#Source: https://stackoverflow.com/questions/60849087/attributeerror-nonetype-object-has-no-attribute-name-error-occurs-when-i-tr
from docx import Document  
document=Document('C:\\Users\\abc\\Desktop\\check\\Leave_Policy_converted.docx')
for paragraph in document.paragraphs:
    if paragraph.style.name == 'Heading 1':
        print (paragraph.text)