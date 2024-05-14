#Source: https://stackoverflow.com/questions/30679134/xlrd-throws-typeerror-embedded-nul-character-when-trying-to-open-an-xls-file
xlfile = 'DJIComponents.xls'
xlbook = xlrd.open_workbook(xlfile)