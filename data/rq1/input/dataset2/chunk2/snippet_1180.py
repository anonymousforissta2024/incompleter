#Source: https://stackoverflow.com/questions/47124194/filenotfounderror-while-scraping-images
# A script to download pictures from reddit.com/r/HistoryPorn
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re
import os
import sys #TODO: sys.argv

print('Downloading images...')

# Create a directory for photographs
path_to_hist = '/home/tautvydas/Documents/histphoto'
os.chdir(path_to_hist)
if not os.path.exists('/home/tautvydas/Documents/histphoto'):
    os.mkdir(path_to_hist)

website = 'https://www.reddit.com/r/HistoryPorn'

# Go to the internet and connect to the subreddit, start a loop
for i in range(3):
    subreddit = urlopen(website)
    bs_subreddit = BeautifulSoup(subreddit, 'lxml')

    # Create a regex and find all the titles in the page
    remove_reddit_tag = re.compile('(\s*\(i.redd.it\)(\s*))')
    title_bs_subreddit = bs_subreddit.findAll('p', {'class': 'title'})

    # Get text off the page
    pic_name = []
    for item in title_bs_subreddit[1:]:
        item = item.get_text()
        item = remove_reddit_tag.sub('', item)
        pic_name.append(item)

    # Get picture links
    pic_bs_subreddit = bs_subreddit.findAll('div', {'data-url' : re.compile('.*')})
    pic_img = []
    for pic in pic_bs_subreddit[1:]:
        pic_img.append(pic['data-url'])

    # Zip all info into one
    name_link = zip(pic_name, pic_img)
    for i in name_link:
        urlretrieve(i[1],i[0])


    # Click next
    for link in bs_subreddit.find('span', {'class' : 'next-button'}).children:
        website = link['href']