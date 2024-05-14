#Source: https://stackoverflow.com/questions/30679134/xlrd-throws-typeerror-embedded-nul-character-when-trying-to-open-an-xls-file
from urllib.request import urlopen
import xlrd
DJIA_URL = 'http://www.djaverages.com/?go=export-components&symbol=DJI'
xlfile = urlopen(DJIA_URL).read()
xlbook = xlrd.open_workbook(xlfile)