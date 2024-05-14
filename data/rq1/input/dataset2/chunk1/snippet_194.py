#Source: https://stackoverflow.com/questions/48591663/python-3-6-typeerror-module-object-is-not-callable
import re
from crawler import Crawler, CrawlerCache

if __name__ == "__main__": 
    # Using SQLite as a cache to avoid pulling twice
    crawler = Crawler(CrawlerCache('crawler.db'))
    root_re = re.compile('^/$').match
    crawler.crawl('http://techcrunch.com/', no_cache=root_re)
    crawler.crawl('http://www.engadget.com/', no_cache=root_re)
    crawler.crawl('http://gizmodo.com/', no_cache=root_re)
    crawler.crawl('http://www.zdnet.com/', no_cache=root_re)
    crawler.crawl('http://www.wired.com/', no_cache=root_re)