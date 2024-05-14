#Source: https://stackoverflow.com/questions/43725686/xlwt-book-save-typeerror-must-be-str-not-bytes
import newspaper
from newspaper import Article

import xlwt

book = xlwt.Workbook()

sheet1 = book.add_sheet("Run1", cell_overwrite_ok=True)

sheet1.write(0, 0, "Text")
sheet1.write(0, 1, "Journalist")
sheet1.write(0, 2, "URL")
sheet1.write(0, 3, "Title")

URL_list=[x,y]

url = URL_list[0]

article = Article(url)

z=1

for n in URL_list:
    sheet1.write(z, 2, n)
    z=z+1

d=1

for n in URL_list:
    url = URL_list[URL_list.index(n)]
    article = Article(url)
    article.download()
    article.parse()
    e = article.title
    sheet1.write(d, 3, e)
    d = d+1

i=1

for n in URL_list:
    url = URL_list[URL_list.index(n)]
    article = Article(url)
    article.download()
    article.parse()
    b = article.text
    sheet1.write(i, 0, b)
    i = i+1

x=1

url = URL_list[0]

article = Article(url)

for n in URL_list:
    url = URL_list[URL_list.index(n)]
    article = Article(url)
    article.download()
    article.parse()
    c = article.authors
    sheet1.write(x, 1, c)
    x = x+1

book.save("Test5_Export_News.xls")