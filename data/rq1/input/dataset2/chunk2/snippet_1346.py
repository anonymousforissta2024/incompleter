#Source: https://stackoverflow.com/questions/64024003/typeerror-nonetype-object-is-not-subscriptable-with-bs4
import sys
from bs4 import BeautifulSoup as Soup

file ="temp.xml"
handler = open(file).read()
soup = Soup(handler,features="lxml")

for vHost in soup.find('virtualhost').find_all('name', string='example.com'):
    print(vHost.parent)#display the right level
    temp=vHost.parent.virtualhost['id']
    print(temp)