#Source: https://stackoverflow.com/questions/74867730/attributeerror-module-bs4-has-no-attribute-beautifulsoup4
import requests,os,bs4
url='http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    print('Загружается страница %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup4(res.text)
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Не удалось найти изображение комиска.')
    else:
        comicUrl = comicElem[0].get('src')
        print('Загружается изображение %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename()
        (comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.close()
        prevLink = soup.select('a[rel]="prev"')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
print('Готово.')