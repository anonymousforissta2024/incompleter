#Source: https://stackoverflow.com/questions/72518657/typeerror-unsupported-operand-types-for-paragraph-and-str-replace-wor
from docx import Document

document = Document('rea.docx')

for paragraph in document.paragraphs:
    if paragraph+'Ocean' in paragraph.text:
        paragraph.text.replace("Sea")