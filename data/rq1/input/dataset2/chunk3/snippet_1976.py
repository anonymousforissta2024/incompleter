#Source: https://stackoverflow.com/questions/63258398/typeerror-cannot-mix-str-and-non-str-arguments
from scrapy import Spider
from scrapy.http import Request


class CourseSpider(Spider):
    name = 'course'
    allowed_domains = ['coursera.org']
    start_urls = ['https://coursera.org/about/partners']

    def parse(self, response):
        listings = response.xpath('//div[@class="rc-PartnerBox vertical-box"]')
        for listing in listings:
            title = listing.xpath('.//div[@class="partner-box-wrapper card-one-clicker flex-1"]/p').extract_first()
            relative_url = listing.xpath('.//a/@href').extract_first()
            absolute_url = response.urljoin(relative_url)

            yield Request(response.urljoin(relative_url), callback = self.parse_listing,meta={'title':title,'absolute_url':absolute_url})

    def parse_listing(self,response):
        titles = response.meta.get('title')
        absolute_url = response.meta.get('absolute_url')
        titles_course =  response.xpath('//div[@class="name headline-1-text"]/text()').extract()
        url_link = response.xpath('//div[@class="rc-Course"]/a/@href').extract()
        abs_url = response.urljoin(url_link)

        yield {'title':title,
        'titles':title,
        'absolute_url':absolute_url,
        'titles_course':titles_course,
        'abs_url':abs_url}