#Source: https://stackoverflow.com/questions/53284528/importing-file-with-constants-and-throwing-attributeerror-python-3
#Currency conversions - dataAccquisition.py

import settings
import requests
from xml.etree import cElementTree as ET
import os
import time

def isDataOld():
    if os.path.isfile(settings.FILE):
        fileTime = os.path.getmtime(settings.FILE)
        if (time.time() - fileTime) / 3600 > 24*1:
            print(' : [MSG] : Data is old.')
            return True
        else:
            print(' : [MSG] : Data is up to date.')
            return False
    print(' : [MSG] : Data does not exist.')
    return True

def getFile():
    if isDataOld():
        print(' : [MSG] : Finding and downloading data from URL.')
        r = requests.get(settings.URL, allow_redirects=True)
        open('exData.xml', 'wb').write(r.content)

def parseData():
    print(' : [MSG] : Starting to parse data...')
    tree = ET.ElementTree(file=settings.FILE)
    root = tree.getroot()
    datalist_currency = []
    datalist_rates    = []
    print(' : [MSG] : Adding currency and rates to datalist=')
    for child in root:
        for subchild in child:
            for subsubchild in subchild:
                print(' : [MSG] : Adding currency',subsubchild.attrib['currency'])
                datalist_currency.append(subsubchild.attrib['currency'])
                print(' : [MSG] : with rate',subsubchild.attrib['rate'])
                datalist_rates.append(subsubchild.attrib['rate'])

    datalist_zip = dict(zip(datalist_currency, datalist_rates))
    print(' : [MSG] : Done parsing data!')
    return datalist_zip