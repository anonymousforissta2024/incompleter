#Source: https://stackoverflow.com/questions/64492779/scrapy-typeerror-can-only-concatenate-str-not-list-to-str
import scrapy
from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
# from urllib.parse import urljoin


class ZomatoSpider(scrapy.Spider):
    name = 'zomato'
    allowed_domain = ['foodbizmalaysia.com']
    start_urls = ['http://www.foodbizmalaysia.com/category/3/bakery-pastry-supplies?classid=DS-B42850']
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "cookie": "dnetsid=5kegaefgfpb0efhf3idfxn30; afrvt=14846924c9bb4e87b5576addf94f8cc4; _ga=GA1.2.1937980614.1603360774; _gid=GA1.2.1358979332.1603360774"
    }


    def parse(self, response):
        url = "http://www.foodbizmalaysia.com/"

        yield scrapy.Request(url, 
            callback=self.parse_api, 
            headers=self.headers)
        


    def parse_api(self, response):
        base_url = 'http://www.foodbizmalaysia.com'
        sel = Selector(response)
        sites = sel.xpath('/html')
                
        for data in sites:
            categories = data.xpath('//div[@class="post_content"]/a[contains(@href, "category")]/@href').extract()
            category_url = base_url + categories

            request = scrapy.Request(
                category_url, 
                callback=self.parse_restaurant_company, 
                headers=self.headers
            ) 

            yield request


    def parse_restaurant_company(self, response):
        base_url = 'http://www.foodbizmalaysia.com'
        sel = Selector(response)
        sites = sel.xpath('/html')

        for data in sites:
            company = data.xpath('//a[contains(@id, "ContentPlaceHolder1_dgrdCompany_Hyperlink4_")]/@href').extract_first()
            company_url = base_url + company
            # for i in company:
            #     yield response.urljoin(
            #         'http://www.foodbizmalaysia.com', i[1:],
            #         callback=self.parse_company_details)

        request = scrapy.Request(
                company_url,
                callback=self.parse_company_details, 
                headers=self.headers

        )
        yield request

    def parse_company_details(self, response):
        sel = Selector(response)
        sites = sel.xpath('/html')

        yield {
            'name' : sites.xpath('//span[@class="coprofileh3"]/text()').get()
        }