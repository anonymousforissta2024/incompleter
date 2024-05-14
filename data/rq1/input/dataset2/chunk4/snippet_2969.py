#Source: https://stackoverflow.com/questions/68474331/scrapy-nameerror-with-item-pipeline-when-calling-from-different-file
#testing.py
import scraper_control
import json

def runScraper(spider):
    sc= scraper_control
    scraper_results = sc.runspider(spider)
    json_result = json.dumps(scraper_results)
    print(json_result)

runScraper("test_quotes")