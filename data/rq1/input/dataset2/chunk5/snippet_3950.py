#Source: https://stackoverflow.com/questions/58086807/typeerror-object-of-type-nonetype-has-no-len-on-python-3-x
from variables import MY_URL , OUT_FILE
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import csv

def agarrar_pagina():

    for i in range(1,22):
        uclient = ureq(MY_URL+'categorias/todas/?page={}'.format(i))
        page_html = uclient.read()
        page_soup = soup(page_html, "html.parser")
        contenedores = page_soup.findAll('div', {'class':'cambur'})
        contenedor=[]
        for link in contenedor:
            link = contenedor.findAll('a',['href'])
            ulink = ureq(MY_URL + link)
            page_link = ulink.read()
            ulink = close()
            uclient.close()

            return page_link