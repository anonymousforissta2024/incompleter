#Source: https://stackoverflow.com/questions/58081123/pdfminer-typeerror-not-all-arguments-converted-during-string-formatting
import sys
from pdfminer.pdfdocument import PDFDocument
from pdfminer.layout import LTContainer, LTComponent, LTRect, LTLine, LAParams, LTTextLine
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.image import ImageWriter
from io import StringIO, BytesIO
from bs4 import BeautifulSoup
import re
import io



def convert_pdf_to_html(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    outfp = BytesIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = HTMLConverter(rsrcmgr, outfp, imagewriter=ImageWriter('out'))
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device) 
    password = ""
    maxpages = 0 #is for all
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

convert_pdf_to_html('PDF - Remraam Ph 1 Mosque.pdf')