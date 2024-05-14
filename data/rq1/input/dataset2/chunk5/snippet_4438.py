#Source: https://stackoverflow.com/questions/59204850/python-error-attributeerror-module-string-has-no-attribute-lstrip
from bs4 import BeautifulSoup
import mechanize
import time
import urllib.request
import string


start = "http://www.irrelevantcheetah.com/browserimages.html"# test website 
filetype = input("What file type are you looking for?\n")

br = mechanize.Browser()
r = br.open(start)
html = r.read()

soup = BeautifulSoup(html, "html5lib")
for link in soup.find_all('a'):
    linkText = str(link)
    fileName = str(link.get('href'))
    if filetype in fileName:
       image = urllib.request.URLopener()
       linkGet = "http://www.irrelevantcheetah.com" + fileName
       filesave = string.lstrip(fileName, '/')
       image.retrieve(linkGet, filesave)