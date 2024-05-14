#Source: https://stackoverflow.com/questions/37369901/attributeerror-httpresponse-object-has-no-attribute-split
import urllib.request
import urllib
from bs4 import BeautifulSoup

symbolsfile = open("Stocklist.txt")

symbolslist = symbolsfile.read()

thesymbolslist = symbolslist.split("\n")

i=0


while i<len (thesymbolslist):
    theurl = "http://www.google.com/finance/getprices?q=" + thesymbolslist[i] + "&i=10&p=25m&f=c"
    thepage = urllib.request.urlopen (theurl)
    print(thesymbolslist[i] + " price is " + thepage.split()[len(thepage.split())-1])
    i= i+1