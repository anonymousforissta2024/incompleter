#Source: https://stackoverflow.com/questions/63823364/exception-has-occurred-typeerror-in-python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

articlelist = []

def request(x):
    url = f'https://www.seaporn.org/category/hevc/page/{x}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, features='lxml')
    return soup.find_all('article', class_ = 'post-summary')

def parse(articles):
    for item in articles:
        link = item.find({'a': 'entry-link'})
        article = {
            'link': link['href']
        }

        articlelist.append(article)

def output():
    df = pd.DataFrame(articlelist)
    df.to_excel('articlelist.xlsx', index=False)
    print('Saved to xlsx.')

x = 5000

while True:
    print(f'Page {x}')
    articles = requests(x)
    x = x + 1
    time.sleep(3)
    if len(articles) != 0:
        parse(articles)
    else:
        break

print('Completed, total articles is', len(articlelist))
output()