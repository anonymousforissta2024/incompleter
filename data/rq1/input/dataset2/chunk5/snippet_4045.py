#Source: https://stackoverflow.com/questions/37503991/error-attributeerror-nonetype-object-has-no-attribute-text
import threading
import requests
from bs4 import BeautifulSoup

symbolsfile = open("Stocklist.txt")

symbolslist = symbolsfile.read()

thesymbolslist = symbolslist.split("\n")

print (thesymbolslist)


print_lock = threading.Lock()

def th(ur):
    theurl = "http://money.cnn.com/quote/quote.html?symb=" + ur
    thepage = requests.get(theurl)
    soup = BeautifulSoup(thepage.content,"html.parser")
    textfind = soup.find('span',{"stream":"last_36276"})
    texttext = textfind.text
    with print_lock:
        print(textfind)

threadlist = []

for u in thesymbolslist:
    t = threading.Thread(target = th, args=(u,))
    t.start()

    threadlist.append(t)

for b in threadlist:
    b.join()