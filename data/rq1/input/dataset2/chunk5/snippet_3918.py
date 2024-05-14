#Source: https://stackoverflow.com/questions/57291114/how-to-add-exception-to-skip-attributeerror-in-my-code
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
urls2 = []
result = requests.get("http://desaku.bandungkab.go.id/desaonline/")
src = result.content
soup = BeautifulSoup(src, 'lxml')
links = soup.find_all('a')
urls = []
for link in links:
    if "www" in link.text:
        url = link.attrs['href']
        urls.append(url)

num1=len(urls)
b=0
while b<10: 
    result2 = requests.get(urls[b])
    src2 = result2.content
    soup = BeautifulSoup(src2, 'lxml')
    links2 = soup.find_all('a')
    for link in links2:
        if "selengkapnya" in link.text:
            url2 = link.attrs['href']
            urls2.append(url2)
    b+=1

num=len(urls2)
i=0
while i<num:
    html = requests.get(urls2[i])
    src = html.content
    soup = BeautifulSoup(src, 'lxml')
    recordList = soup.findAll("div", {"class": "artikel", })
    recordlist = soup.find_all('div', attrs={'class':'sampul2'})

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='bs4-test',
                                 charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            for record in recordList:
    #except AttributeError:
                #continue #WHERE TO PUT THIS EXCEPTION,TO SKIP ATRRIBUTEERRROR?
                title = record.find("h2", {"class": "judul",      }).get_text().strip()
                date = record.find('i').next_sibling.next_sibling.next_sibling.replace('\t\t\t\t\t\t\t', '')
                content = record.find("div", {"class":"teks"}).get_text().strip()
                image = record.img['src']
                cover = record.img['src']
                sql = "INSERT INTO `artikel` (`jdl`, `tgl`, `kon`, `gambar`, `sampul`) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (title, date, content, image, cover))
        connection.commit()
        print ("Record inserted successfully into table")
    finally:
        connection.close()
        print("MySQL connection is closed")
    i+=1