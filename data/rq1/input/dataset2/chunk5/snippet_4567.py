#Source: https://stackoverflow.com/questions/65702068/error-attributeerror-nonetype-object-has-no-attribute-find
import requests
import lxml
import bs4

title = ''
date = ''
text = ''
top = []
link = []  


web_link = 'https://timesofindia.indiatimes.com/{}/'
web_link = web_link.format('india')
req = requests.get(web_link)
soup = bs4.BeautifulSoup(req.text, 'lxml')
topi = soup.find('div', {'class':'main-content'})
topi = topi.find_all('span', {'class':'w_tle'})
for i in range(len(topi)):
   top = topi[i].find('a').get('href')
   link.append('https://timesofindia.indiatimes.com' + top)
for i in range(len(link)):
   rq = requests.get(link[i])
   sp = bs4.BeautifulSoup(rq.text, 'lxml')
   title = sp.find('div', {'class':'_2NFXP'})
   title = title.find('h1',{'class':'_23498'})