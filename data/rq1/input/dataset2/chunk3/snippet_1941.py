#Source: https://stackoverflow.com/questions/66566100/attributeerror-object-has-no-attribute-published-when-parsing-cnn-source
import feedparser

url = "http://rss.cnn.com/rss/edition.rss"
feed = feedparser.parse(url)
for news in feed.entries:
    print(news.published)