#Source: https://stackoverflow.com/questions/52169355/bs4-attributeerror-nonetype-object-has-no-attribute-text
import bs4 as bs
import urllib.request
import csv

with open('C:/Users/******/Desktop/urls.csv', 'r') as f:
    reader = csv.reader(f)
    pages = list(reader)
    for i in range (0,300):
        page = ''.join(map(str, pages[i]))
        print('Working on ' + str(i)+ "...")
        sauce = urllib.request.urlopen(page).read()
        soup =bs.BeautifulSoup(sauce,'lxml')
        textoffer = soup.body.div.find('div',class_='jobsearch-JobComponent-description icl-u-xs-mt--md').text
        file = open(str(i)+ '.txt','w')
        file.write(textoffer)
        file.close()
        print(str(i) + " Done!")