#Source: https://stackoverflow.com/questions/60941433/iterating-through-a-dictionary-typeerror-list-indices-must-be-integers-or-slic
# -*- coding: utf-8 -*-
import scrapy
from ..items import JobcollectorItem
from ..AutoCrawler import searchIndeed


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    page_number = 2
    start_urls = [searchIndeed.current_page_url]

    def parse(self, response):
        items = JobcollectorItem()

        position = response.css('.jobtitle::text').extract()
        company = response.css('span.company::text').extract()
        location = response.css('.location::text').extract()

        # print(position[0])

        items['position'] = position
        items['company'] = company
        items['location'] = location

        for key in items.keys():
            prestripped = items[key]
            for object in prestripped:
                object = object.strip('\n')
            items[key] = prestripped

        yield items