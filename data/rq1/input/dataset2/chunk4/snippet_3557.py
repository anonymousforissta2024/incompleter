#Source: https://stackoverflow.com/questions/75851013/reoccuring-attributeerror-nonetype-object-has-no-attribute-find-all
for i in range(10,140,20):
     url = (f'https://www.indeed.com/cmp/Ey/reviews?fcountry=IT&start={i}')
     header = {'User-Agent':'Mozilla/5.0 Gecko/20100101 Firefox/33.0 GoogleChrome/10.0'}
     page = requests.get(url,headers = header)
     soup = BeautifulSoup(page.content, 'lxml')
     results = soup.find('div', { 'id' : 'cmp-container'})
     elems = results.find_all(class_="cmp-Review-container")