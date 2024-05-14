#Source: https://stackoverflow.com/questions/51087973/attribute-error-none-type-object-has-no-attribute-get-text
import urllib.request
from bs4 import BeautifulSoup
import pymysql.cursors

a = input ('enter the item to be searched :')
a = a.replace(" ","")

html = urllib.request.urlopen("https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+a)

bsObj = BeautifulSoup(html,'lxml')
recordList = bsObj.findAll('a', class_='a-link-normal a-text-normal')

connection = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         db='shopping',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        for record in recordList:
            name = record.find("h2", {"class": "a-size-small a-color-base s-inline  s-access-title  a-text-normal", }).get_text().strip()
            sale_price = record.find("span", {"class": "currencyINR"}).get_text().strip()
            category = record.find("span", {"class": "a-color-base a-text-bold"}).get_text().strip()
            sql = "INSERT INTO `amazon` (`name`, `sale_price`, `category`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, sale_price, category))
    connection.commit()
finally:
    connection.close()