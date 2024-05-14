#Source: https://stackoverflow.com/questions/68474331/scrapy-nameerror-with-item-pipeline-when-calling-from-different-file
#scraper_control.py
spiders = {"test_quotes": ToScrapeCSSSpider}
items = []

class ItemCollectorPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        items.append(item)

crawler_process = CrawlerProcess(
    {
        "USER_AGENT": "scrapy",
        "LOG_LEVEL": "INFO",
        "ITEM_PIPELINES": {"__main__.ItemCollectorPipeline": 100},
    }
)

def runspider(spider):
    crawler_process.crawl(spiders[spider])
    crawler_process.start()
    return items