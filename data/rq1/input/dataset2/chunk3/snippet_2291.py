#Source: https://stackoverflow.com/questions/69480350/typeerror-selector-object-is-not-iterable
from scrapy import Spider


class WikiSpider(Spider):
    name = 'wiki'
    allowed_domains = ['wikipedia.com']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States']

    def parse(self, response):
        Tabel=response.xpath('//table[contains(@class,"wikitable sortable")]')[0]
        for tabel in Tabel:        
          state=tabel.xpath('.//tbody/tr/th/a/text()')[1:].extract()
          yield{
                state
            }
         