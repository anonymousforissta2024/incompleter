#Source: https://stackoverflow.com/questions/59444515/attributeerror-nonetype-object-has-no-attribute-html
from facebook_scraper import get_posts
import csv
import pandas as pd
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
csvFile = open('nintendo.csv', 'a')
csvWriter = csv.writer(csvFile)
for post in get_posts('nintendo', pages=100):
    print(post['text'].translate(non_bmp_map))
    csvWriter.writerow([post['text'].encode('utf-8')])